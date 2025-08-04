from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define the Python function for the PythonOperator
def log_python_message():
    print("🔁 PythonOperator executed successfully!")

# Default arguments for the DAG
default_args = {
    'owner': 'sanjusci',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
with DAG(
    dag_id='day2_bash_python_dag',
    default_args=default_args,
    description='Day 2: Demonstrate PythonOperator and BashOperator with chaining',
    start_date=datetime(2025, 8, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['day2', 'airflow-learning', 'operators']
) as dag:

    # Python task
    python_task = PythonOperator(
        task_id='run_python_function',
        python_callable=log_python_message
    )

    # Bash task to print date
    bash_task = BashOperator(
        task_id='print_date',
        bash_command='echo "📅 Today\'s date is: $(date)"'
    )

    # Bash task to simulate delay
    sleep_task = BashOperator(
        task_id='sleep_task',
        bash_command='sleep 5'
    )

    # Define task dependencies (chaining)
    python_task >> bash_task >> sleep_task
