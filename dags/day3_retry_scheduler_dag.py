from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import random

# --------------------------
# Default arguments for DAG
# --------------------------
default_args = {
    'owner': 'sanjusci',                      # DAG owner name
    'retries': 2,                            # Number of retries if task fails
    'retry_delay': timedelta(minutes=1),     # Wait time between retries
    'sla': timedelta(minutes=5),             # SLA: task should finish within 5 minutes
}

# --------------------------------
# DAG definition and configuration
# --------------------------------
with DAG(
    dag_id='day3_retry_scheduler_dag',
    default_args=default_args,
    description='Day 3 - Retry, Catchup, SLA, Execution Timing',
    schedule_interval='@daily',              # Run once a day
    start_date=datetime(2025, 8, 1),         # Start date of DAG
    catchup=False,                           # Skip backfilling past runs
    tags=['day3', 'airflow-learning', 'Retry'],       # Optional tags for filtering in UI
) as dag:

    # ---------------------------
    # Python task that may fail
    # ---------------------------
    def fail_randomly(**context):
        execution_date = context['ds']  # 'ds' = execution date as YYYY-MM-DD
        print(f"Task execution date: {execution_date}")

        # Simulate failure randomly (50% chance)
        if random.choice([True, False]):
            raise Exception("❌ Simulated failure for retry testing.")
        else:
            print("✅ Task succeeded.")

    fail_task = PythonOperator(
        task_id='fail_task',
        python_callable=fail_randomly,   # Function to execute
        provide_context=True,            # Required to access `context['ds']`
    )

    # ---------------------------
    # Bash task that always runs
    # ---------------------------
    success_task = BashOperator(
        task_id='success_task',
        bash_command='echo "✅ Success after retry or first attempt."'  # Simple bash print
    )

    # ---------------------------
    # Set task dependencies
    # ---------------------------
    fail_task >> success_task   # success_task runs only after fail_task succeeds
