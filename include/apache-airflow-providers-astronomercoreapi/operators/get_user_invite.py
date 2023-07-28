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


class GetUserInviteOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        invite_id: Annotated[
            StrictStr, Field(..., description="invite ID or auth0 ticket ID")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.invite_id = invite_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_user_invite(
            invite_id=self.invite_id,
        )
        self.log.info(response)
        return response

