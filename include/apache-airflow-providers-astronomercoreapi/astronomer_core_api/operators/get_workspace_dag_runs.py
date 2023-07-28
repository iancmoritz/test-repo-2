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


class GetWorkspaceDagRunsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID that defines the workspace")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the DAG runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the DAG runs metrics in seconds"),
        ],
        deployment_ids: Annotated[
            Optional[StrictStr],
            Field(description="IDs that define the deployments, separated by comma"),
        ],
        virtual_runtime_ids: Annotated[
            Optional[StrictStr],
            Field(
                description="IDs that define the virtual runtimes, separated by comma"
            ),
        ],
        runtime_type: Annotated[
            Optional[StrictStr], Field(description="type of runtime")
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.range = range
        self.step = step
        self.deployment_ids = deployment_ids
        self.virtual_runtime_ids = virtual_runtime_ids
        self.runtime_type = runtime_type
        self.status = status
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_workspace_dag_runs(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            range=self.range,
            step=self.step,
            deployment_ids=self.deployment_ids,
            virtual_runtime_ids=self.virtual_runtime_ids,
            runtime_type=self.runtime_type,
            status=self.status,
        )
        self.log.info(response)
        return response

