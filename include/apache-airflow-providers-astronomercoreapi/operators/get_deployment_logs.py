from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from airflow.models import BaseOperator
from hooks.astronomer_core_api_api import AstronomerCoreApiHook


from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint, conlist

if TYPE_CHECKING:
    from airflow.utils.context import Context

logger = logging.getLogger(__name__)


class GetDeploymentLogsOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr, Field(..., description="deployment ID to get logs from")
        ],
        sources: Annotated[
            conlist(StrictStr),
            Field(..., description="log sources to select logs from"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="limit of the count of the logs"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset of the log entries"),
        ],
        range: Annotated[
            Optional[conint(strict=True, ge=60)],
            Field(description="range of the log search in seconds"),
        ],
        max_num_results: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="maximum number of results across all pages"),
        ],
        search_id: Annotated[
            Optional[StrictStr], Field(description="searchId to get logs from")
        ],
        search_text: Annotated[
            Optional[StrictStr],
            Field(description="an exact text search param used to filter the data on"),
        ],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.organization_id = organization_id
        self.deployment_id = deployment_id
        self.sources = sources
        self.limit = limit
        self.offset = offset
        self.range = range
        self.max_num_results = max_num_results
        self.search_id = search_id
        self.search_text = search_text
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_deployment_logs(
            organization_id=self.organization_id,
            deployment_id=self.deployment_id,
            sources=self.sources,
            limit=self.limit,
            offset=self.offset,
            range=self.range,
            max_num_results=self.max_num_results,
            search_id=self.search_id,
            search_text=self.search_text,
        )
        self.log.info(response)
        return response

