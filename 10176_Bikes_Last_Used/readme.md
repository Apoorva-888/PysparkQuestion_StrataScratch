# 10176_Bikes_Last_Used

**Platform:** StrataScratch  
**Difficulty:** Easy  
**Question ID:** 10176  

🔗 Question Link: [StrataScratch Question](https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=6)

---

## Problem Summary

Find the **last time each bike was in use**.  

- Output columns:
  - `bike_number`  
  - `last_used` → the date-time the bike was returned (`end_time`)  
- Order results by bikes **most recently used first**.  

Sample output (first 5 rows):

| bike_number | last_used           |
|------------|-------------------|
| W01278     | 2012-03-31 19:28:00|
| W01097     | 2012-03-31 15:37:00|
| W00270     | 2012-03-31 12:10:00|
| W01006     | 2012-03-31 10:44:00|
| W01242     | 2012-03-31 09:24:00|

---

## Table

### dc_bikeshare_q1_2012

| Column            | Type      |
|------------------|-----------|
| duration          | string    |
| duration_seconds  | bigint    |
| start_time        | timestamp |
| start_station     | string    |
| start_terminal    | bigint    |
| end_time          | timestamp |
| end_station       | string    |
| end_terminal      | bigint    |
| bike_number       | string    |
| rider_type        | string    |
| id                | bigint    |

---

## Approach

1. Use **groupBy** on `bike_number`.  
2. Find the **maximum `end_time`** for each bike to get the last used time.  
3. Rename the column to `last_used`.  
4. Order results by `last_used` descending.  

This is a simple aggregation using PySpark's DataFrame API.

---

## Technologies Used

- PySpark  
- DataFrame API  
- Aggregation functions (`max`)  


