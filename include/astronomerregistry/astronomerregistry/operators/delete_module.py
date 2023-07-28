from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_registry_api import AstronomerRegistryHook


from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class DeleteModuleOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr,
            Field(..., description="The name or display name of the provider"),
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the module, or keyword 'latest' for latest version",
            ),
        ],
        module_name: Annotated[
            StrictStr, Field(..., description="The name of the module")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.org_short_name_id = org_short_name_id
        self.provider_name = provider_name
        self.version = version
        self.module_name = module_name
        self.hook: AstronomerRegistryHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.delete_module(
            org_short_name_id=self.org_short_name_id,
            provider_name=self.provider_name,
            version=self.version,
            module_name=self.module_name,
        )
        self.log.info(response)
        return response

