### ✅ Day 3: Scheduling & Dependencies

#### 📘 Learnings

Today you will explore:

- How DAGs are scheduled using **cron expressions**
- Task **retry behavior** with delay
- Defining dependencies via `>>`, `set_upstream()`, and `set_downstream()`
- Introduction to **SLAs** (Service Level Agreements)

---

#### ⏰ Scheduling

- Airflow allows flexible scheduling using **cron** or predefined values:
  - `@daily`, `@hourly`, `@weekly`, etc.
- Example: Run every day at 9:30 AM:
  ```python
  schedule_interval='30 9 * * *'
