from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetSelfUserOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        create_if_not_exist: Annotated[
            Optional[StrictBool],
            Field(description="create self user if it does not already exist"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.create_if_not_exist = create_if_not_exist
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_self_user(
            create_if_not_exist=self.create_if_not_exist,
        )
        self.log.info(response)
        return response

