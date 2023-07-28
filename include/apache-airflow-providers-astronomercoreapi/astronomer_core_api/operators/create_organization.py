from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook

from astronomer_core_api.sdk.models import (
    CreateOrganizationRequest,
)

from typing_extensions import Annotated
from pydantic import Field

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class CreateOrganizationOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        body: Annotated[
            CreateOrganizationRequest,
            Field(..., description="request body for creating an organization"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.body = body
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.create_organization(
            body=self.body,
        )
        self.log.info(response)
        return response
