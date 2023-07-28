from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from astronomer_core_api.operators.list_dags import ListDagsOperator

@dag(
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
)
def simple_task_group() -> None:
    """
    The simplest example of using Cosmos to render a dbt project as a TaskGroup.
    """
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    list_dags_task = ListDagsOperator(
        task_id="list_dags_task",
        conn_id="astronomer-registry",
        organization_id="something-something",
        deployment_ids=["something-something"],
        workspace_ids=["something-something"],
        offset=0,
        limit=100,
        sorts=["dag_id:asc"])
    
    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> list_dags_task >> post_dbt


simple_task_group()