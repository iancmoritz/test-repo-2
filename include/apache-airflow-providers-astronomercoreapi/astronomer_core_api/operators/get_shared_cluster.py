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


class GetSharedClusterOperator(BaseOperator):
    def __init__(
        self,
        conn_id: str,
        region: Annotated[StrictStr, Field(..., description="region")],
        cloud_provider: Annotated[StrictStr, Field(..., description="cloud provider")],
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.region = region
        self.cloud_provider = cloud_provider
        self.hook: AstronomerCoreApiHook(conn_id=conn_id)

    def execute(self, context: Context) -> None:
        response = self.hook.get_shared_cluster(
            region=self.region,
            cloud_provider=self.cloud_provider,
        )
        self.log.info(response)
        return response

