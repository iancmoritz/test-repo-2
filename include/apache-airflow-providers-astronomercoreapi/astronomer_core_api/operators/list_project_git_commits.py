from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListProjectGitCommitsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="Workspace ID that the project belong to")
        ],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        branch: Annotated[
            Optional[StrictStr],
            Field(
                description="The branch to list commits for, if different to the project's branch"
            ),
        ],
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page number for pagination"),
        ],
        per_page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page size for pagination"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.branch = branch
        self.page = page
        self.per_page = per_page
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_project_git_commits(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            branch=self.branch,
            page=self.page,
            per_page=self.per_page,
        )
        self.log.info(response)
        return response

