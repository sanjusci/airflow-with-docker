## ✅ Day 4: XComs, Variables & Branching

### 📚 Learnings
- **XComs**: Cross-task communication using push/pull methods.
- **Variables**: Store environment-specific or configurable values.
- **Branching**: Use logic to conditionally execute specific tasks.

---

### 🗂️ DAG File
- `day4_xcom_branch_dag.py`

---

### 📊 Task Flow
```mermaid
graph TD;
    push_xcom --> branch_task;
    branch_task --> task_true;
    branch_task --> task_false;
    task_true --> join;
    task_false --> join;
