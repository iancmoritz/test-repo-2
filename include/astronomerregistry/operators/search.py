from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_registry_api import AstronomerRegistryHook

from client.astronomerregistry.models import (
    RegistrySearchRequest,
)

from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class SearchOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        body: Annotated[
            RegistrySearchRequest,
            Field(..., description="request body for a registry search"),
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified providers")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured providers")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global providers")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private providers")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible providers"),
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
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'. Default to searchRank:asc"
            ),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.org_short_name_id = org_short_name_id
        self.body = body
        self.is_certified = is_certified
        self.is_featured = is_featured
        self.is_global = is_global
        self.is_private = is_private
        self.is_cloud_ide_compatible = is_cloud_ide_compatible
        self.offset = offset
        self.limit = limit
        self.sorts = sorts
        self.hook: AstronomerRegistryHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.search(
            org_short_name_id=self.org_short_name_id,
            body=self.body,
            is_certified=self.is_certified,
            is_featured=self.is_featured,
            is_global=self.is_global,
            is_private=self.is_private,
            is_cloud_ide_compatible=self.is_cloud_ide_compatible,
            offset=self.offset,
            limit=self.limit,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

