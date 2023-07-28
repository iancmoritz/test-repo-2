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


class ListWorkspaceUsersOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing users"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.offset = offset
        self.limit = limit
        self.sorts = sorts
        self.search = search
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_workspace_users(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            offset=self.offset,
            limit=self.limit,
            sorts=self.sorts,
            search=self.search,
        )
        self.log.info(response)
        return response
