from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetPipelineOperator(BaseOperator):
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
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.pipeline_id = pipeline_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_pipeline(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            pipeline_id=self.pipeline_id,
        )
        self.log.info(response)
        return response

