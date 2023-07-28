from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook

from client.astronomercoreapi.models import (
    MutateWorkspaceUserRoleRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class MutateWorkspaceUserRoleOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
        body: Annotated[
            MutateWorkspaceUserRoleRequest,
            Field(
                ..., description="request body for mutating an organization user role"
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.user_id = user_id
        self.body = body
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.mutate_workspace_user_role(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            user_id=self.user_id,
            body=self.body,
        )
        self.log.info(response)
        return response

