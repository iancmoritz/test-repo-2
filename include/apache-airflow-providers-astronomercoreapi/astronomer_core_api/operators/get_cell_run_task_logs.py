from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetCellRunTaskLogsOperator(BaseOperator):
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
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        cell_run_id: Annotated[StrictStr, Field(..., description="ID of the cell run")],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
        var_from: Annotated[
            Optional[StrictInt], Field(description="The line number to start from")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.project_id = project_id
        self.pipeline_id = pipeline_id
        self.cell_id = cell_id
        self.cell_run_id = cell_run_id
        self.task_id = task_id
        self.var_from = var_from
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_cell_run_task_logs(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            project_id=self.project_id,
            pipeline_id=self.pipeline_id,
            cell_id=self.cell_id,
            cell_run_id=self.cell_run_id,
            task_id=self.task_id,
            var_from=self.var_from,
        )
        self.log.info(response)
        return response

