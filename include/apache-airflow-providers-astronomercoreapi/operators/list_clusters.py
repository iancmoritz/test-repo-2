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


class ListClustersOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        provider: Annotated[
            Optional[StrictStr],
            Field(description="cloud provider to filter clusters on"),
        ],
        types: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="type to filter clusters on"),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status to filter clusters on")
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing clusters"),
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
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.provider = provider
        self.types = types
        self.status = status
        self.search = search
        self.offset = offset
        self.limit = limit
        self.sorts = sorts
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_clusters(
            organization_id=self.organization_id,
            provider=self.provider,
            types=self.types,
            status=self.status,
            search=self.search,
            offset=self.offset,
            limit=self.limit,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

