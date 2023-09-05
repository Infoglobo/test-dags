from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1
}


with DAG(
    dag_id="example_kubernetes_pod", schedule="@once", default_args=default_args
) as dag:
    KubernetesPodOperator(
        namespace="airflow-prd",
        image="hello-world",
        name="airflow-test-pod",
        task_id="task-one",
        is_delete_operator_pod=True,
        get_logs=True,
    )