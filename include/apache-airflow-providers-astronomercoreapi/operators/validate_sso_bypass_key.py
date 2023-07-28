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


class ValidateSsoBypassKeyOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        sso_bypass_key: Annotated[
            StrictStr, Field(..., description="SSO bypass key for organization")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.sso_bypass_key = sso_bypass_key
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.validate_sso_bypass_key(
            sso_bypass_key=self.sso_bypass_key,
        )
        self.log.info(response)
        return response

