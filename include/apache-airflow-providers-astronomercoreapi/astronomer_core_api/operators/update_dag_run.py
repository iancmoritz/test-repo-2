from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from astronomer_core_api.hooks.astronomer_core_api_api import AstronomerCoreApiHook

from astronomer_core_api.sdk.models import (
    UpdateDagRunRequest,
)

from typing_extensions import Annotated
from pydantic import Field, StrictStr

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class UpdateDagRunOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        data: Annotated[
            UpdateDagRunRequest,
            Field(..., description="request body for updating a dag run"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.workspace_id = workspace_id
        self.runtime_id = runtime_id
        self.dag_id = dag_id
        self.dag_run_id = dag_run_id
        self.data = data
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.update_dag_run(
            organization_id=self.organization_id,
            workspace_id=self.workspace_id,
            runtime_id=self.runtime_id,
            dag_id=self.dag_id,
            dag_run_id=self.dag_run_id,
            data=self.data,
        )
        self.log.info(response)
        return response

