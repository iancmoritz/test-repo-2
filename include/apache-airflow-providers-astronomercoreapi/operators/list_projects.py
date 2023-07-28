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


class ListProjectsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Workspace IDs that projects belong to"),
        ],
        include_pipeline_counts: Annotated[
            Optional[StrictBool],
            Field(description="Include pipeline counts for each project"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="search string across name and description"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_ids = workspace_ids
        self.include_pipeline_counts = include_pipeline_counts
        self.offset = offset
        self.limit = limit
        self.search = search
        self.sorts = sorts
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_projects(
            organization_id=self.organization_id,
            workspace_ids=self.workspace_ids,
            include_pipeline_counts=self.include_pipeline_counts,
            offset=self.offset,
            limit=self.limit,
            search=self.search,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

