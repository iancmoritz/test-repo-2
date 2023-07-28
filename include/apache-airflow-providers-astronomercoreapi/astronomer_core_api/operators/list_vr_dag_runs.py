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


class ListVrDagRunsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
        state: Annotated[
            Optional[StrictStr],
            Field(
                description="list of state of dag runs, separated by comma (OR condition)"
            ),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date greater than or equal to specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date less than or equal to specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date greater than or equal to specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date less than or equal to specified date"
            ),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date greater than or equal to specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date less than or equal to specified date"
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.virtual_runtime_id = virtual_runtime_id
        self.dag_id = dag_id
        self.offset = offset
        self.limit = limit
        self.order_by = order_by
        self.state = state
        self.execution_date_gte = execution_date_gte
        self.execution_date_lte = execution_date_lte
        self.start_date_gte = start_date_gte
        self.start_date_lte = start_date_lte
        self.end_date_gte = end_date_gte
        self.end_date_lte = end_date_lte
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_vr_dag_runs(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            virtual_runtime_id=self.virtual_runtime_id,
            dag_id=self.dag_id,
            offset=self.offset,
            limit=self.limit,
            order_by=self.order_by,
            state=self.state,
            execution_date_gte=self.execution_date_gte,
            execution_date_lte=self.execution_date_lte,
            start_date_gte=self.start_date_gte,
            start_date_lte=self.start_date_lte,
            end_date_gte=self.end_date_gte,
            end_date_lte=self.end_date_lte,
        )
        self.log.info(response)
        return response

