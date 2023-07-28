from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetTaskInstanceLogsOperator(BaseOperator):
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
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        dag_task_id: Annotated[
            StrictStr, Field(..., description="ID of the dag run task")
        ],
        dag_task_try_number: Annotated[
            StrictInt, Field(..., description="ID of the dag run task try number")
        ],
        full_content: Annotated[
            Optional[StrictBool], Field(description="task log full content")
        ],
        map_index: Annotated[
            Optional[StrictInt], Field(description="task map index for mapped task")
        ],
        token: Annotated[
            Optional[StrictStr],
            Field(description="token that allows you to continue fetching logs"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.runtime_id = runtime_id
        self.dag_id = dag_id
        self.dag_run_id = dag_run_id
        self.dag_task_id = dag_task_id
        self.dag_task_try_number = dag_task_try_number
        self.full_content = full_content
        self.map_index = map_index
        self.token = token
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_task_instance_logs(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            runtime_id=self.runtime_id,
            dag_id=self.dag_id,
            dag_run_id=self.dag_run_id,
            dag_task_id=self.dag_task_id,
            dag_task_try_number=self.dag_task_try_number,
            full_content=self.full_content,
            map_index=self.map_index,
            token=self.token,
        )
        self.log.info(response)
        return response

