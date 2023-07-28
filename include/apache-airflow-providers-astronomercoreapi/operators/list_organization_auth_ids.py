from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListOrganizationAuthIdsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        email: Annotated[
            StrictStr,
            Field(..., description="User email to retrieve organization auth IDs for"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.email = email
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_organization_auth_ids(
            email=self.email,
        )
        self.log.info(response)
        return response

