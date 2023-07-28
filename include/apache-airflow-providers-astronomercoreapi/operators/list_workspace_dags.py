from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListWorkspaceDagsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        page_size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="page size, default of 20"),
        ],
        order_by: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="order-by fields, comma separated"),
        ],
        cursor: Annotated[Optional[StrictStr], Field(description="pagination cursor")],
        num_runs: Annotated[
            Optional[conint(strict=True, le=50, ge=0)],
            Field(description="number of runs to include per dag, default of 0"),
        ],
        name: Annotated[
            Optional[StrictStr], Field(description="filter by name of DAG (dagId)")
        ],
        name__like: Annotated[
            Optional[StrictStr],
            Field(
                description="filter by pattern for name of DAG (dagId),  SQL  syntax"
            ),
        ],
        owner: Annotated[
            Optional[StrictStr], Field(description="filter by an owner of the dag")
        ],
        is_paused: Annotated[
            Optional[StrictBool], Field(description="filter by paused dags")
        ],
        is_active: Annotated[
            Optional[StrictBool], Field(description="filter by active dags")
        ],
        last_run_state__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="filter by dag runs with any of these run states for its last run"
            ),
        ],
        run_state__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dag runs with any of these run states"),
        ],
        run_after: Annotated[
            Optional[datetime],
            Field(
                description="filter by dag run after specified datetime (RFC3339 format)"
            ),
        ],
        tag__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by any of these tags"),
        ],
        deployment_id__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by any of these deployment IDs"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.page_size = page_size
        self.order_by = order_by
        self.cursor = cursor
        self.num_runs = num_runs
        self.name = name
        self.name__like = name__like
        self.owner = owner
        self.is_paused = is_paused
        self.is_active = is_active
        self.last_run_state__in = last_run_state__in
        self.run_state__in = run_state__in
        self.run_after = run_after
        self.tag__in = tag__in
        self.deployment_id__in = deployment_id__in
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_workspace_dags(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            page_size=self.page_size,
            order_by=self.order_by,
            cursor=self.cursor,
            num_runs=self.num_runs,
            name=self.name,
            name__like=self.name__like,
            owner=self.owner,
            is_paused=self.is_paused,
            is_active=self.is_active,
            last_run_state__in=self.last_run_state__in,
            run_state__in=self.run_state__in,
            run_after=self.run_after,
            tag__in=self.tag__in,
            deployment_id__in=self.deployment_id__in,
        )
        self.log.info(response)
        return response

