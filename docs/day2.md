### ✅ Day 2: Operators (Python & Bash)

#### 📘 Learnings

Today, you will learn how to use two core operators in Apache Airflow:

- **PythonOperator**: Executes a custom Python function.
- **BashOperator**: Runs shell commands.

You’ll also learn to **chain tasks** using `>>` to define execution order.

---

#### 🔧 Operators

- **PythonOperator**
  - Takes a `python_callable` (function name).
  - Runs any Python logic (e.g., print logs, data checks).

- **BashOperator**
  - Takes a `bash_command`.
  - Executes shell scripts like `echo`, `sleep`, or any CLI tool.

---

#### 🔗 Task Chaining

You can chain tasks like:
```python
task1 >> task2 >> task3
