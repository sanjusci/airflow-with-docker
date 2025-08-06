## 🐍 `day4_xcom_branch_dag.py` – Python DAG
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import Variable
from datetime import datetime, timedelta

# --------------------------
# Default arguments for DAG
# --------------------------
default_args = {
    'owner': 'sanjusci',                      # DAG owner name
    'retries': 2,                            # Number of retries if task fails
    'retry_delay': timedelta(minutes=1),     # Wait time between retries
}

# Define the DAG
with DAG(
    dag_id='day4_xcom_branch_dag',
    start_date=datetime(2025, 8, 5),
    schedule_interval='@daily',
    catchup=False,
    tags=['day4', 'xcom', 'variables', 'branching', 'airflow-learning'],
    default_args=default_args,
    description="XComs, Variables, and Branching Example",
) as dag:

    # 🧪 Task 1: Push a value using XCom (simulates upstream computation)
    def push_value(**context):
        value = "prod"  # This could come from any business logic
        # Push the value to XCom with a key
        context['ti'].xcom_push(key='env_key', value=value)
        print(f"[push_xcom] Pushed value: {value}")

    push_xcom = PythonOperator(
        task_id='push_xcom',
        python_callable=push_value,
        provide_context=True  # Required to access context['ti']
    )

    # 🔀 Task 2: Branch based on XCom value or Airflow Variable
    def choose_branch(**context):
        # Try to get value from Airflow Variable named 'env'
        env = Variable.get("env", default_var=None)

        # If Variable isn't set, fallback to XCom
        if env is None:
            env = context['ti'].xcom_pull(task_ids='push_xcom', key='env_key')

        print(f"[branch_task] Branching based on value: {env}")

        # Return the next task ID based on condition
        return 'task_true' if env == 'prod' else 'task_false'

    branch_task = BranchPythonOperator(
        task_id='branch_task',
        python_callable=choose_branch,
        provide_context=True
    )

    # ✅ Task 3a: Runs if environment is 'prod'
    task_true = PythonOperator(
        task_id='task_true',
        python_callable=lambda: print("✅ Running task for PROD environment.")
    )

    # 🚫 Task 3b: Runs if environment is anything else
    task_false = PythonOperator(
        task_id='task_false',
        python_callable=lambda: print("⚠️ Not running PROD tasks.")
    )

    # 🔁 Task 4: Dummy task to join both branches
    join = DummyOperator(
        task_id='join',
        trigger_rule='none_failed_min_one_success'  # Join path regardless of which branch was taken
    )

    # Set task execution order using bitshift (>>) operators
    push_xcom >> branch_task >> [task_true, task_false] >> join
