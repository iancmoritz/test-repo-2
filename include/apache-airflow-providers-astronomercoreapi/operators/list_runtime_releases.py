from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook



if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListRuntimeReleasesOperator(BaseOperator):
    def __init__(self, conn_id: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_runtime_releases()
        self.log.info(response)
        return response

