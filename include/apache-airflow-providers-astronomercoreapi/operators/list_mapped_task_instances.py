from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional, Union
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListMappedTaskInstancesOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=0)],
            Field(description="limit for pagination"),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is greater or equal to the specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is less than or equal to the specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="start date is greater than or equal to the specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(description="start date is less than or equal to the specified date"),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="end date is greater than or equal to the specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(description="end date is less than or equal to the specified date"),
        ],
        duration_gte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is greater than or equal to the specified in seconds"
            ),
        ],
        duration_lte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is less than or equal to the specified in seconds"
            ),
        ],
        states: Annotated[
            Optional[conlist(StrictStr)], Field(description="task states")
        ],
        pools: Annotated[Optional[conlist(StrictStr)], Field(description="task pools")],
        queues: Annotated[
            Optional[conlist(StrictStr)], Field(description="task queues")
        ],
        order_by: Annotated[
            Optional[StrictStr],
            Field(
                description="The name of the field to order the results by. Prefix a field name with - to reverse the sort order."
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.task_id = task_id
        self.workspace_id = workspace_id
        self.runtime_id = runtime_id
        self.dag_id = dag_id
        self.dag_run_id = dag_run_id
        self.offset = offset
        self.limit = limit
        self.execution_date_gte = execution_date_gte
        self.execution_date_lte = execution_date_lte
        self.start_date_gte = start_date_gte
        self.start_date_lte = start_date_lte
        self.end_date_gte = end_date_gte
        self.end_date_lte = end_date_lte
        self.duration_gte = duration_gte
        self.duration_lte = duration_lte
        self.states = states
        self.pools = pools
        self.queues = queues
        self.order_by = order_by
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_mapped_task_instances(
            organization_id=self.organization_id,
            task_id=self.task_id,
            workspace_id=self.workspace_id,
            runtime_id=self.runtime_id,
            dag_id=self.dag_id,
            dag_run_id=self.dag_run_id,
            offset=self.offset,
            limit=self.limit,
            execution_date_gte=self.execution_date_gte,
            execution_date_lte=self.execution_date_lte,
            start_date_gte=self.start_date_gte,
            start_date_lte=self.start_date_lte,
            end_date_gte=self.end_date_gte,
            end_date_lte=self.end_date_lte,
            duration_gte=self.duration_gte,
            duration_lte=self.duration_lte,
            states=self.states,
            pools=self.pools,
            queues=self.queues,
            order_by=self.order_by,
        )
        self.log.info(response)
        return response

