from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.hooks.postgres_hook import PostgresHook
import logging
import datetime

class CustomLogOperator(BaseOperator):

    @apply_defaults
    def __init__(self, log_message, log_to='file', pg_conn_id='postgres_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_message = log_message
        self.log_to = log_to
        self.pg_conn_id = pg_conn_id

    def execute(self, context):
        timestamp = datetime.datetime.utcnow().isoformat()
        full_log = f"[{timestamp}] {self.log_message}"

        if self.log_to == 'file':
            with open('/opt/airflow/logs/custom_log.txt', 'a') as f:
                f.write(full_log + '\n')
            print("Log written to file.")

        elif self.log_to == 'postgres':
            hook = PostgresHook(postgres_conn_id=self.pg_conn_id)
            hook.run("CREATE TABLE IF NOT EXISTS custom_logs (timestamp TIMESTAMPTZ, message TEXT);")
            hook.run(
                "INSERT INTO custom_logs (timestamp, message) VALUES (%s, %s);",
                parameters=(timestamp, self.log_message)
            )
            print(f"Log written to Postgres. {full_log}")

        else:
            raise ValueError("Invalid log target. Use 'file' or 'postgres'.")
