# ✅ Day 6: Custom Operators & Hooks

---

## 🎯 Goal

- Learn how to **build a custom operator** in Airflow.
- Understand and use **Hooks**, such as `PostgresHook` and `HttpHook`.
- Implement a DAG that **logs messages to a file or PostgreSQL** via a custom operator.

---

## 📚 What You Will Learn

- Creating a custom operator (`CustomLogOperator`)
- Using Airflow’s `BaseOperator` and `apply_defaults`
- Connecting to Postgres using `PostgresHook`
- Writing logs either to a file or into a database table
- Creating a DAG that chains custom logging tasks

---

## 📁 Files

- DAG file: [`day6_custom_operator_dag.py`](../dags/day6_custom_operator_dag.py)
- Custom Operator: [`custom_log_operator.py`](../plugins/operators/custom_log_operator.py)

---

## 🧠 Key Concepts

### ✅ Custom Operator

An operator is a Python class that performs a single task. You can subclass `BaseOperator` to create your own.

```python
class CustomLogOperator(BaseOperator):
    def __init__(self, log_message, log_to='file', pg_conn_id='postgres_default', *args, **kwargs):
        ...
```
# 🌐 How to Add Connections in Airflow Admin UI

Airflow uses **Connections** to interact with external systems like databases, APIs, cloud providers, and more. You can add or edit these via the **Airflow Web UI**.

---

## 🛠️ Steps to Add a Connection in Airflow

### ✅ 1. Open Airflow UI

- Navigate to: [http://localhost:8080](http://localhost:8080)
- Login if required (default: username = `airflow`, password = `airflow`)

---

### ✅ 2. Go to **Admin → Connections**

- Click on **"Admin"** (top menu)
- Select **"Connections"**

![Admin > Connections](../images/admin_connections.png) <!-- Replace with actual image -->

---

### ✅ 3. Click **"+ Add a new record"**

- Located at the top right of the Connections page
- Opens a form to enter new connection details

---

## 🔌 Common Connection Examples

---

### 🔗 **PostgreSQL Connection**

| Field         | Value                  |
|---------------|------------------------|
| Conn Id       | `postgres_default`     |
| Conn Type     | `Postgres`             |
| Host          | `postgres`             |
| Schema        | `airflow`              |
| Login         | `airflow`              |
| Password      | `airflow`              |
| Port          | `5432`                 |

---

### 🔗 **HTTP API Connection**

| Field         | Value                     |
|---------------|---------------------------|
| Conn Id       | `http_api`                |
| Conn Type     | `HTTP`                    |
| Host          | `https://jsonplaceholder.typicode.com` |
| Extra         | (leave empty)             |

---

### 🔗 **Google Cloud (GCP) Connection**

| Field         | Value                     |
|---------------|---------------------------|
| Conn Id       | `google_cloud_default`    |
| Conn Type     | `Google Cloud`            |
| Project Id    | `your-project-id`         |
| Keyfile Path  | `/path/to/keyfile.json`   |
| Scopes        | `https://www.googleapis.com/auth/cloud-platform` |

---

## ✅ 4. Save the Connection

Click **"Save"** at the bottom to store the connection.

You can now use this `conn_id` in:
- Operators (e.g., `PostgresOperator`, `HttpOperator`, `BigQueryOperator`)
- Hooks (e.g., `PostgresHook`, `HttpHook`, `GCSHook`)

---

## 📌 Notes

- Airflow connections are stored in its metadata database.
- You can also create connections using CLI or ENV variables (`AIRFLOW_CONN_*`).
- Avoid using `localhost` as host — use Docker service names inside containers (e.g., `postgres`, `gcs`, etc.)

---

## 📎 Optional: Create via CLI

```bash
airflow connections add 'postgres_default' \
    --conn-type 'postgres' \
    --conn-host 'postgres' \
    --conn-login 'airflow' \
    --conn-password 'airflow' \
    --conn-schema 'airflow' \
    --conn-port 5432
```
# 🧪 How to Check PostgreSQL Connection Inside Docker (Airflow)

When using Airflow and Postgres in Docker, it’s important to verify that the **PostgreSQL service is accessible from your containers**, especially for tasks using `PostgresOperator` or `PostgresHook`.

---

## ✅ Option 1: Use `psql` Inside the Airflow Container

### 🔹 Step 1: Enter the Airflow container

```bash
docker exec -it <container-id> bash
```

### 🔹 Step 2: Use `psql` to connect to Postgres
```bash
psql -h postgres -U airflow -d airflow
```