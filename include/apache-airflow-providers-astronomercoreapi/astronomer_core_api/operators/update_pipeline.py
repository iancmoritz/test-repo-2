from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook

from astronomer_core_api.sdk.models import (
    UpdatePipelineRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class UpdatePipelineOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[StrictStr, Field(..., description="ID of the project")],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        data: Annotated[
            UpdatePipelineRequest,
            Field(..., description="request body for updating a pipeline"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.pipeline_id = pipeline_id
        self.data = data
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.update_pipeline(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            pipeline_id=self.pipeline_id,
            data=self.data,
        )
        self.log.info(response)
        return response

