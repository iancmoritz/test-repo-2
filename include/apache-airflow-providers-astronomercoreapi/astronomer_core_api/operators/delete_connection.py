from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class DeleteConnectionOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        connection_id: Annotated[
            StrictStr, Field(..., description="ID of the connection")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.virtual_runtime_id = virtual_runtime_id
        self.connection_id = connection_id
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.delete_connection(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            virtual_runtime_id=self.virtual_runtime_id,
            connection_id=self.connection_id,
        )
        self.log.info(response)
        return response

