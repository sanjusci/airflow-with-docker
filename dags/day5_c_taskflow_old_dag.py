import json
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


def extract():
    # Old way: simulate extracting data from a JSON string
    data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
    return json.loads(data_string)


def transform(ti):
    # Old way: manually pull from XCom
    order_data_dict = ti.xcom_pull(task_ids="extract")
    total_order_value = sum(order_data_dict.values())
    return {"total_order_value": total_order_value}


def load(ti):
    # Old way: manually pull from XCom
    total = ti.xcom_pull(task_ids="transform")["total_order_value"]
    print(f"Total order value is: {total:.2f}")


with DAG(
        dag_id="legacy_etl_pipeline",
        default_args={'owner': 'sanjusci', 'retries': 1, 'retry_delay': pendulum.duration(minutes=5)},
        description="Legacy ETL pipeline using PythonOperator",
        schedule=None,
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        tags=["example"],
) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    load_task = PythonOperator(task_id="load", python_callable=load)

    extract_task >> transform_task >> load_task
