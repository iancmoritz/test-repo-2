from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetDeploymentsTaskRunsPerStatusOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the task runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the task runs metrics in seconds"),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status of task runs")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.deployment_id = deployment_id
        self.range = range
        self.step = step
        self.status = status
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_deployments_task_runs_per_status(
            organization_id=self.organization_id,
            deployment_id=self.deployment_id,
            range=self.range,
            step=self.step,
            status=self.status,
        )
        self.log.info(response)
        return response

