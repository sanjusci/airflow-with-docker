### ✅ Day 1: Introduction to Airflow, DAG Basics & Scheduling

#### 📘 What is Apache Airflow?
Apache Airflow is an open-source platform to **programmatically author, schedule, and monitor workflows**. These workflows are defined as **DAGs (Directed Acyclic Graphs)** and are useful for automating ETL, ML, and other data pipeline tasks.

---

#### 📌 What is a DAG?
A **DAG** is a collection of tasks that run in a specific order without any cycles. Each DAG defines:
- `dag_id`: Unique identifier
- `start_date`: When the DAG starts
- `schedule_interval`: Frequency of runs (e.g., `@daily`)
- `default_args`: Default parameters for all tasks
- `tasks`: Nodes that perform specific actions (Python, Bash, etc.)

---

#### 🕒 Scheduling in Airflow
- **`schedule_interval`** — Defines how often the DAG runs (`@daily`, `@hourly`, cron format)
- **`start_date`** — Sets when Airflow starts scheduling the DAG
- **`catchup=False`** — Prevents Airflow from running past missed schedules
- **Manual Trigger** — DAGs can also be run manually via the Airflow UI

---

#### 🧪 Example DAG Schedule
```python
schedule_interval = "@daily"
start_date = datetime(2025, 8, 1)
