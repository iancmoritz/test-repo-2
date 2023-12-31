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


class ListRuntimesOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where runtimes belong to"
            ),
        ],
        runtime_type: Annotated[
            Optional[StrictStr],
            Field(description="runtimeType to filter runtimes with"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        release_names: Annotated[
            Optional[StrictStr],
            Field(
                description="release names to filter runtimes with, separated by comma"
            ),
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
        self.runtime_type = runtime_type
        self.offset = offset
        self.limit = limit
        self.release_names = release_names
        self.sorts = sorts
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_runtimes(
            organization_id=self.organization_id,
            workspace_ids=self.workspace_ids,
            runtime_type=self.runtime_type,
            offset=self.offset,
            limit=self.limit,
            release_names=self.release_names,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

