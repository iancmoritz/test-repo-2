from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from astronomerregistry.operators import list_dags

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

    list_dags_task = list_dags(
        conn_id="astronomer-registry",
        org_short_name_id="public")
    
    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> list_dags_task >> post_dbt


simple_task_group()