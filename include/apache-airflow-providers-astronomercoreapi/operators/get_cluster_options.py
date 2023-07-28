from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetClusterOptionsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        type: Annotated[StrictStr, Field(..., description="cluster type")],
        provider: Annotated[Optional[StrictStr], Field(description="cloud provider")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.type = type
        self.provider = provider
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_cluster_options(
            type=self.type,
            provider=self.provider,
        )
        self.log.info(response)
        return response

