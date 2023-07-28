from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class ListVrImportErrorsOperator(BaseOperator):
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
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.virtual_runtime_id = virtual_runtime_id
        self.offset = offset
        self.limit = limit
        self.order_by = order_by
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.list_vr_import_errors(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            virtual_runtime_id=self.virtual_runtime_id,
            offset=self.offset,
            limit=self.limit,
            order_by=self.order_by,
        )
        self.log.info(response)
        return response

