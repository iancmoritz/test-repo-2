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


class ListProjectGitBranchesOperator(BaseOperator):
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
        repo: Annotated[
            Optional[StrictStr],
            Field(description="a repo to override the project's repo"),
        ],
        vendor: Annotated[
            Optional[StrictStr],
            Field(description="a vendor to override the project's git vendor"),
        ],
        azure_dev_ops_organization: Annotated[
            Optional[StrictStr],
            Field(
                description="an Azure DevOps organization to override the project's git vendor attributes"
            ),
        ],
        azure_dev_ops_project_id: Annotated[
            Optional[StrictStr],
            Field(
                description="an Azure DevOps project ID to override the project's git vendor attributes"
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
        x_git_token: Annotated[
            Optional[StrictStr],
            Field(description="a token to override the project's token"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.repo = repo
        self.vendor = vendor
        self.azure_dev_ops_organization = azure_dev_ops_organization
        self.azure_dev_ops_project_id = azure_dev_ops_project_id
        self.page = page
        self.per_page = per_page
        self.x_git_token = x_git_token
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_project_git_branches(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            repo=self.repo,
            vendor=self.vendor,
            azure_dev_ops_organization=self.azure_dev_ops_organization,
            azure_dev_ops_project_id=self.azure_dev_ops_project_id,
            page=self.page,
            per_page=self.per_page,
            x_git_token=self.x_git_token,
        )
        self.log.info(response)
        return response

