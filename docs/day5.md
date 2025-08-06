# ✅ Day 5: TaskFlow API & Sensors

## 📚 Learnings
- Understand how to use the **TaskFlow API** in Airflow using `@task` decorators
- Work with **Sensors**:
  - `FileSensor` – to wait for the presence of a file in the filesystem
  - `ExternalTaskSensor` – to wait for another DAG’s task to finish (not covered in this example, but mentioned)

## 📄 DAG: `day5_taskflow_sensor_dag.py`

### 🧠 Tasks:
1. **Wait for a file** using `FileSensor`
2. **Process the file** using TaskFlow `@task`
3. **Log the result**

## 📂 DAG Structure:
```text
file_sensor >> process_file
