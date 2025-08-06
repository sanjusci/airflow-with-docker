import os
import sys
from airflow import DAG
from datetime import datetime, timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), '../plugins'))

from operators.custom_log_operator import CustomLogOperator
# This DAG demonstrates the use of a custom operator to log messages to either a file or a PostgreSQL database.
default_args = {
    'owner': 'sanjusci',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 8, 1),
    'catchup': False
}

with DAG('day6_custom_operator_dag',
         default_args=default_args,
         schedule_interval="@daily",
         description='DAG using custom operator to log to file or DB',
         tags=['airflow-learning', 'custom', 'hooks']) as dag:

    log_to_file = CustomLogOperator(
        task_id='log_to_file',
        log_message='This is a log message written to a file.',
        log_to='file'
    )

    log_to_postgres = CustomLogOperator(
        task_id='log_to_postgres',
        log_message='This is a log message written to PostgreSQL.',
        log_to='postgres',
        pg_conn_id='postgres_default'
    )

    log_to_postgres >> log_to_file
