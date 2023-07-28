from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_registry_api import AstronomerRegistryHook


from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class DeleteDagOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        dag_name: Annotated[StrictStr, Field(..., description="The name of the dag")],
        version: Annotated[StrictStr, Field(..., description="The version of the dag")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.org_short_name_id = org_short_name_id
        self.dag_name = dag_name
        self.version = version
        self.hook: AstronomerRegistryHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.delete_dag(
            org_short_name_id=self.org_short_name_id,
            dag_name=self.dag_name,
            version=self.version,
        )
        self.log.info(response)
        return response

