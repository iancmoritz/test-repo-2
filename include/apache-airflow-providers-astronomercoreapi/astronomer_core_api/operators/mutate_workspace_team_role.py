from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook

from astronomer_core_api.sdk.models import (
    MutateWorkspaceTeamRoleRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class MutateWorkspaceTeamRoleOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        body: Annotated[
            MutateWorkspaceTeamRoleRequest,
            Field(..., description="request body for mutating a workspace team role"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.team_id = team_id
        self.body = body
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.mutate_workspace_team_role(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            team_id=self.team_id,
            body=self.body,
        )
        self.log.info(response)
        return response

