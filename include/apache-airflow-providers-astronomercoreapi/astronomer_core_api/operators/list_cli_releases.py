from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook



if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListCliReleasesOperator(BaseOperator):
    def __init__(self, conn_id: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_cli_releases()
        self.log.info(response)
        return response

