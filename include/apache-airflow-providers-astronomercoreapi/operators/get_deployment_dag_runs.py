from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetDeploymentDagRunsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID to query for dags structure"),
        ],
        dag_id: Annotated[StrictStr, Field(..., description="dagId of the dags")],
        page_size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="page size, default of 20"),
        ],
        cursor: Annotated[Optional[StrictStr], Field(description="pagination cursor")],
        run_id: Annotated[
            Optional[StrictStr], Field(description="filter by ID of the dags run")
        ],
        logical_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by logical date (aka execution date)  of  the  dags  run  less     than  (RFC3339 format)"
            ),
        ],
        logical_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by logical date (aka execution date)  of  the  dags  run  greater  than  (RFC3339 format)"
            ),
        ],
        start_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by start date of the dags run less than (RFC3339 format)"
            ),
        ],
        start_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by start date of the dags run greater than (RFC3339 format)"
            ),
        ],
        end_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by end date of the dags run less than (RFC3339 format)"
            ),
        ],
        end_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by end date of the dags run greater than (RFC3339 format)"
            ),
        ],
        state: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dags runs with any of these run states"),
        ],
        run_type__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dags runs with any of these run types"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.deployment_id = deployment_id
        self.dag_id = dag_id
        self.page_size = page_size
        self.cursor = cursor
        self.run_id = run_id
        self.logical_date__lt = logical_date__lt
        self.logical_date__gt = logical_date__gt
        self.start_date__lt = start_date__lt
        self.start_date__gt = start_date__gt
        self.end_date__lt = end_date__lt
        self.end_date__gt = end_date__gt
        self.state = state
        self.run_type__in = run_type__in
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_deployment_dag_runs(
            organization_id=self.organization_id,
            deployment_id=self.deployment_id,
            dag_id=self.dag_id,
            page_size=self.page_size,
            cursor=self.cursor,
            run_id=self.run_id,
            logical_date__lt=self.logical_date__lt,
            logical_date__gt=self.logical_date__gt,
            start_date__lt=self.start_date__lt,
            start_date__gt=self.start_date__gt,
            end_date__lt=self.end_date__lt,
            end_date__gt=self.end_date__gt,
            state=self.state,
            run_type__in=self.run_type__in,
        )
        self.log.info(response)
        return response

