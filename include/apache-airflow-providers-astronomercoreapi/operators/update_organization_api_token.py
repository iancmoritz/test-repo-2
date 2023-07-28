from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook

from client.astronomercoreapi.models import (
    UpdateOrganizationApiTokenRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class UpdateOrganizationApiTokenOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
        body: Annotated[
            UpdateOrganizationApiTokenRequest,
            Field(
                ..., description="request body for updating an organization API token"
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.api_token_id = api_token_id
        self.body = body
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.update_organization_api_token(
            organization_id=self.organization_id,
            api_token_id=self.api_token_id,
            body=self.body,
        )
        self.log.info(response)
        return response

