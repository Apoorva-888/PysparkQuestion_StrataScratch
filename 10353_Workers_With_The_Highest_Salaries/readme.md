# Workers With The Highest Salaries

**Platform:** StrataScratch  
**Difficulty:** Easy  
**Question ID:** 10353  

🔗 Question Link: [StrataScratch Question](https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=6)

---

## Problem Summary

Management wants to analyze employees with **official job titles only**.  
You need to find the **job titles** of employees with the **highest salary**.  

- If multiple employees share the highest salary, include all their job titles.  
- Output column: `best_paid_title`  
- Sample output:

| best_paid_title |
|----------------|
| Asst. Manager  |
| Manager        |

---

## Tables

### worker

| Column        | Type    |
|---------------|---------|
| worker_id     | bigint  |
| first_name    | string  |
| last_name     | string  |
| salary        | bigint  |
| joining_date  | date    |
| department    | string  |

### title

| Column        | Type    |
|---------------|---------|
| worker_ref_id | bigint  |
| worker_title  | string  |
| affected_from | date    |

---

## Approach

1. **Join** `worker` and `title` tables to include only employees with official job titles.  
2. Use a **window function** to rank employees by salary in descending order.  
3. Use `dense_rank()` to handle ties for the highest salary.  
4. Filter employees with `dense_rank = 1`.  
5. Select `worker_title` and rename as `best_paid_title`.  
6. Remove duplicates using `.distinct()`.  

This approach is **fully distributed** and avoids pulling data to the driver.

---

## Technologies Used

- PySpark  
- Window Functions  
- DataFrame API  

