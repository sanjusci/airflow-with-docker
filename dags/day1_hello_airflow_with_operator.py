"""
DAG demonstrating the use of PythonOperator in Apache Airflow.

This DAG contains three tasks:
- print_hello: Prints a hello message.
- get_name: Greets a user by name.
- get_current_date: Prints the current date.

Author: Sanjusci
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    return 'Hello from Airflow!'


def get_name(name):
    return f'Hello {name}!'


def get_current_date():
    return f'Today is {datetime.today().strftime("%Y-%m-%d")}'


default_args = {
    'owner': 'sanjusci',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        'day1_hello_airflow',
        default_args=default_args,
        description='Our first dag using python operator',
        schedule_interval='@daily',
        start_date=datetime(2025, 8, 1),
        catchup=False,
        tags=['day1', 'airflow-learning', 'DAG-Basics'],
) as dag:
    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
        op_kwargs={'name': 'Airflow User'}
    )

    task3 = PythonOperator(
        task_id='get_date',
        python_callable=get_current_date,
    )

    task1 >> task2 >> task3
