# 📅 Apache Airflow – 7-Day Learning Plan (Day-Wise Breakdown)

Welcome to the structured **7-day day-wise Apache Airflow learning track**. This guide is designed for developers, data engineers, or analysts who want to learn and practice workflow orchestration using Airflow.

Each day focuses on a core concept with hands-on DAG examples inside the `/dags/` directory.

---

## 🛠️ How to Use This

- Make sure you have Airflow running (see [Main README](README.md) for setup via Docker).
- Navigate to `dags/` and enable the DAG for each day via the Airflow UI.
- Follow the concepts and try modifying DAGs to experiment and learn more.

---

## 📅 Day-by-Day Plan

### ✅ Day 1: [Introduction to Airflow & DAGs](./docs/day1.md)
- Learn: What is Airflow, DAG basics, scheduling
- DAG: `day1_hello_airflow_with_operator.py`
- Task: Print “Hello from Airflow”

---

### ✅ Day 2: Operators (Python & Bash)
- Learn: PythonOperator, BashOperator, chaining tasks
- DAG: `day2_bash_python_dag.py`
- Task: Run Python function → Bash command → Sleep

---

### ✅ Day 3: Scheduling & Dependencies
- Learn: DAG scheduling (cron), retries, `set_upstream()`, SLAs
- DAG: `day3_retry_scheduler_dag.py`
- Task: Fail intentionally and observe retry behavior

---

### ✅ Day 4: XComs, Variables & Branching
- Learn: XCom push/pull, Airflow Variables, Branching logic
- DAG: `day4_xcom_branch_dag.py`
- Task: Pass value between tasks and trigger conditional path

---

### ✅ Day 5: TaskFlow API & Sensors
- Learn: TaskFlow API decorators, FileSensor, ExternalTaskSensor
- DAG: `day5_taskflow_sensor_dag.py`
- Task: Wait for a file → Process it → Log result

---

### ✅ Day 6: Custom Operators & Hooks
- Learn: Build your own operator, use Hooks (PostgresHook, HttpHook)
- DAG: `day6_custom_operator_dag.py`
- Task: Log something to file or DB using custom operator

---

### ✅ Day 7: Mini Project – ETL Pipeline
- Learn: Combining concepts into a real-world DAG
- DAG: `day7_etl_project_dag.py`
- Task: Extract from API → Transform data → Load to DB → Email on success

---
Here is a sample `README.md` for running Apache Airflow with Docker. It explains the setup, usage, and basic commands.

```
# Apache Airflow with Docker

This project provides a quick way to run Apache Airflow using Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Initialize Airflow:**
   ```
   mkdir -p ./dags ./logs ./plugins
   echo -e "AIRFLOW_UID=$(id -u)" > .env
   ```

3. **Start Airflow:**
   ```
   docker compose up airflow-init
   docker compose up
   ```

4. **Access the Airflow UI:**
   - Open your browser and go to: [http://localhost:8001](http://localhost:8001)
   - Default credentials:  
     - Username: `airflow`  
     - Password: `airflow`

## Useful Commands

- **Stop Airflow:**
  ```
  docker compose down
  ```

- **View logs:**
  ```
  docker compose logs
  ```

- **Run a bash shell in the webserver:**
  ```
  docker compose exec airflow-webserver bash
  ```

## Folder Structure

- `dags/` - Place your DAG files here.
- `logs/` - Airflow logs.
- `plugins/` - Custom plugins.

## References

- [Airflow Official Docker Docs](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

---

**Note:**  
Modify the `docker-compose.yml` as needed for your project requirements.
```
7-Day Apache Airflow Learning Plan (with Projects)