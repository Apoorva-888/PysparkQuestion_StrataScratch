# Finding Updated Records

Platform: StrataScratch  
Difficulty: Easy  
Question ID: 10299  

🔗 Question Link: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=6

## Problem Summary

We have a table containing employee salary history.
Some records are outdated because salary increases every year.

Goal:
Find the latest (current) salary for each employee and return:

- id
- first_name
- last_name
- department_id
- current salary

Results must be ordered by employee id ascending.

## Approach

- Salary increases over time → highest salary is the current salary
- Use window function partitioned by employee id
- Keep only the row with highest salary
- Order final output by id

## Technologies Used

- PySpark
- Window Functions
