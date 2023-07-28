from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListOrganizationsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing users"),
        ],
        trial_status: Annotated[
            Optional[StrictStr],
            Field(description="filter by trial status, null for all orgs"),
        ],
        support_plan: Annotated[
            Optional[StrictStr],
            Field(
                description="filter by support plan, should be one of INTERNAL, POV, TRIAL, BASIC, STANDARD, PREMIUM, BUSINESS_CRITICAL, or null for all orgs"
            ),
        ],
        product: Annotated[
            Optional[StrictStr],
            Field(description="filter by product, null for all orgs"),
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
        self.search = search
        self.trial_status = trial_status
        self.support_plan = support_plan
        self.product = product
        self.sorts = sorts
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_organizations(
            search=self.search,
            trial_status=self.trial_status,
            support_plan=self.support_plan,
            product=self.product,
            sorts=self.sorts,
        )
        self.log.info(response)
        return response

