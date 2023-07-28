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


class GetMappedTaskInstanceOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        task_id: Annotated[StrictStr, Field(..., description="task ID")],
        map_index: Annotated[StrictStr, Field(..., description="task map index")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.runtime_id = runtime_id
        self.dag_id = dag_id
        self.dag_run_id = dag_run_id
        self.task_id = task_id
        self.map_index = map_index
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_mapped_task_instance(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            runtime_id=self.runtime_id,
            dag_id=self.dag_id,
            dag_run_id=self.dag_run_id,
            task_id=self.task_id,
            map_index=self.map_index,
        )
        self.log.info(response)
        return response

