from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListDeploymentsDagRunsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
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
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.range = range
        self.step = step
        self.deployment_ids = deployment_ids
        self.workspace_ids = workspace_ids
        self.offset = offset
        self.limit = limit
        self.sorts = sorts
        self.status = status
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_deployments_dag_runs(
            organization_id=self.organization_id,
            range=self.range,
            step=self.step,
            deployment_ids=self.deployment_ids,
            workspace_ids=self.workspace_ids,
            offset=self.offset,
            limit=self.limit,
            sorts=self.sorts,
            status=self.status,
        )
        self.log.info(response)
        return response

