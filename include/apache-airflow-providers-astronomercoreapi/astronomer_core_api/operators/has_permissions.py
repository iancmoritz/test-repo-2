from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook

from astronomer_core_api.sdk.models import (
    HasPermissionsRequest,
)

from typing_extensions import Annotated
from pydantic import Field

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class HasPermissionsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        body: Annotated[
            HasPermissionsRequest,
            Field(..., description="request body for get permissions"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.body = body
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.has_permissions(
            body=self.body,
        )
        self.log.info(response)
        return response

