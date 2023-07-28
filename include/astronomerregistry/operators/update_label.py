from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_registry_api import AstronomerRegistryHook

from client.astronomerregistry.models import (
    UpdateLabelRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class UpdateLabelOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the label")
        ],
        label_name: Annotated[
            StrictStr, Field(..., description="The name of the label")
        ],
        body: Annotated[
            UpdateLabelRequest,
            Field(..., description="request body for updating a registry label"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.org_short_name_id = org_short_name_id
        self.label_group = label_group
        self.label_name = label_name
        self.body = body
        self.hook: AstronomerRegistryHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.update_label(
            org_short_name_id=self.org_short_name_id,
            label_group=self.label_group,
            label_name=self.label_name,
            body=self.body,
        )
        self.log.info(response)
        return response
