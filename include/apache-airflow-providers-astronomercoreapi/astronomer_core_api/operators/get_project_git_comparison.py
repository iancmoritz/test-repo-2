from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetProjectGitComparisonOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        branch: Annotated[
            Optional[StrictStr],
            Field(
                description="The branch to compare against, if different to the project's branch"
            ),
        ],
        exclude_config: Annotated[
            Optional[StrictBool],
            Field(description="Whether to exclude config files from the comparison"),
        ],
        pipeline_id: Annotated[
            Optional[StrictStr],
            Field(description="only include changes for this pipeline"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.branch = branch
        self.exclude_config = exclude_config
        self.pipeline_id = pipeline_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_project_git_comparison(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            branch=self.branch,
            exclude_config=self.exclude_config,
            pipeline_id=self.pipeline_id,
        )
        self.log.info(response)
        return response

