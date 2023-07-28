from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_registry_api import AstronomerRegistryHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListModulesOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified modules")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured modules")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global modules")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private modules")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible modules"),
        ],
        type_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one type in input filter list"),
        ],
        tier_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier in input filter list"),
        ],
        category_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category in input filter list"),
        ],
        badge_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge in input filter list"),
        ],
        dag_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one id in input filter list"),
        ],
        module_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one module in input filter list"),
        ],
        provider_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one provider in input filter list"),
        ],
        tier_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier name in input filter list"),
        ],
        category_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category name in input filter list"),
        ],
        badge_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge name in input filter list"),
        ],
        provider_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one provider name in input filter list"),
        ],
        query: Annotated[
            Optional[StrictStr], Field(description="Search query for module")
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
        self.org_short_name_id = org_short_name_id
        self.is_certified = is_certified
        self.is_featured = is_featured
        self.is_global = is_global
        self.is_private = is_private
        self.is_cloud_ide_compatible = is_cloud_ide_compatible
        self.type_name = type_name
        self.tier_id = tier_id
        self.category_id = category_id
        self.badge_id = badge_id
        self.dag_id = dag_id
        self.module_id = module_id
        self.provider_id = provider_id
        self.tier_name = tier_name
        self.category_name = category_name
        self.badge_name = badge_name
        self.provider_name = provider_name
        self.query = query
        self.offset = offset
        self.limit = limit
        self.sorts = sorts
        self.hook: AstronomerRegistryHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_modules(
            org_short_name_id=self.org_short_name_id,
            is_certified=self.is_certified,
            is_featured=self.is_featured,
            is_global=self.is_global,
            is_private=self.is_private,
            is_cloud_ide_compatible=self.is_cloud_ide_compatible,
            type_name=self.type_name,
            tier_id=self.tier_id,
            category_id=self.category_id,
            badge_id=self.badge_id,
            dag_id=self.dag_id,
            module_id=self.module_id,
            provider_id=self.provider_id,
            tier_name=self.tier_name,
            category_name=self.category_name,
            badge_name=self.badge_name,
            provider_name=self.provider_name,
            query=self.query,
            offset=self.offset,
            limit=self.limit,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

