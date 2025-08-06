"""
Day 5: TaskFlow API & FileSensor DAG

This DAG demonstrates:
1. Use of the TaskFlow API via the `@task` decorator.
2. Waiting for a file to appear using `FileSensor`.
3. Reading and printing the file content once available.

Prerequisites:
- Create a filesystem connection named 'fs_default' in Airflow Admin UI.
- Mount or ensure the file path '/opt/airflow/dags/data/input.txt' is accessible inside your Airflow container.

Author: Sanjusci<sanju.sci9@gmail.com>
"""

from airflow import DAG
from airflow.decorators import task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

# --------------------------
# Default arguments for DAG
# --------------------------
default_args = {
    'owner': 'sanjusci',  # DAG owner name
    'retries': 2,  # Number of retries if task fails
    'retry_delay': timedelta(minutes=1),  # Wait time between retries
}

# -----------------------------------------------------------------------------------
# DAG definition
# -----------------------------------------------------------------------------------

with DAG(
        dag_id="day5_taskflow_sensor_dag",
        default_args=default_args,
        description="Demonstration of FileSensor and TaskFlow API to read file content",
        start_date=datetime(2025, 8, 6),  # DAG start date (past to ensure trigger)
        schedule_interval="@daily",  # Run daily
        catchup=False,  # Prevent backfilling old runs
        tags=["day5", "airflow-learning", "taskflow", "sensor"],
) as dag:
    # --------------------------------------------------------------------------------
    # Task 1: Wait for a file to appear in a specific location using FileSensor
    # --------------------------------------------------------------------------------
    wait_for_file = FileSensor(
        task_id="file_sensor_task",
        fs_conn_id=None,  # Use default filesystem connection
        filepath="data/input.txt",  # Relative path under DAGs folder inside container
        poke_interval=30,  # Wait 30s between checks
        timeout=600,  # Timeout after 10 minutes
        mode="poke",  # "poke" blocks the worker until the condition is met
        doc_md="""
        #### 📄 FileSensor Task

        This task checks for the presence of the file `data/input.txt` every 30 seconds.
        It will timeout if not found within 10 minutes.

        - `fs_conn_id` must point to a valid File System connection.
        - File path is relative to the DAGs folder.
        """,
    )


    # --------------------------------------------------------------------------------
    # Task 2: Process the file using TaskFlow API
    # --------------------------------------------------------------------------------
    @task(
        task_id="read_file_task",
        doc_md="""
        #### 🧾 Read File Task

        This task reads the content of `input.txt` and logs it.

        It assumes the file was mounted properly in the `./data/` directory.
        """
    )
    def process_file():
        """
        Reads a text file from a mounted volume and logs its contents.

        Raises:
            FileNotFoundError: If the file is missing.
            IOError: If file reading fails.
        """
        file_path = "data/input.txt"  # Relative path to the file
        try:
            with open(file_path, "r") as f:
                content = f.read()
                print(f"✅ File content:\n{content}")
        except FileNotFoundError:
            print(f"❌ File not found at path: {file_path}")
            raise
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            raise


    # --------------------------------------------------------------------------------
    # DAG task flow: Wait for file → Process it
    # --------------------------------------------------------------------------------
    wait_for_file >> process_file()
