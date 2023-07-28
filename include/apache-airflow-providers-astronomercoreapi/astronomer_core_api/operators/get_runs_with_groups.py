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


class GetRunsWithGroupsOperator(BaseOperator):
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
        root: Annotated[
            Optional[StrictStr],
            Field(description="name of parent task to get grid data for"),
        ],
        run_state: Annotated[
            Optional[StrictStr], Field(description="run state to filter on")
        ],
        run_type: Annotated[
            Optional[StrictStr], Field(description="run type to filter on")
        ],
        base_date: Annotated[Optional[datetime], Field(description="base date")],
        num_runs: Annotated[
            Optional[StrictStr],
            Field(description="number of runs to select grid data for"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.runtime_id = runtime_id
        self.dag_id = dag_id
        self.root = root
        self.run_state = run_state
        self.run_type = run_type
        self.base_date = base_date
        self.num_runs = num_runs
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_runs_with_groups(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            runtime_id=self.runtime_id,
            dag_id=self.dag_id,
            root=self.root,
            run_state=self.run_state,
            run_type=self.run_type,
            base_date=self.base_date,
            num_runs=self.num_runs,
        )
        self.log.info(response)
        return response

