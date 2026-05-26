# Pandas_Practice_Questions


I am practicing the Pandas library to improve my skills and build confidence.


---

## 📌 Questions List


### 1️⃣ Employees from IT Department (Pandas)
- **File:** `employees_from_it_department.py`
- **Problem:** Show only employees belonging to the IT department.
- **Concepts:** DataFrame filtering, Boolean indexing
---

### 2️⃣ Sales Employees with Salary > 39000 (Pandas)
- **File:** `employees_sales_salary_gt_39000.py`
- **Problem:** Show employees from Sales department whose salary is greater than 39000.
- **Concepts:** Multiple conditions, Boolean indexing, AND operator

---

### 3️⃣ Sort Employees by Salary and Experience (Pandas)
- **File:** `sort_employees_by_salary_experience.py`
- **Problem:** Sort employees by salary in descending order and experience in ascending order.
- **Concepts:** sort_values, multiple columns, ascending/descending order

---

### 4️⃣ Count Missing Values in Each Column (Pandas)
- **File:** `check_missing_values.py`
- **Problem:** Find the total number of missing (NULL) values in each column.
- **Concepts:** isnull(), sum(), handling missing data


---

### 5️⃣ Fill Missing Sales Values with Average (Pandas)
- **File:** `fill_missing_sales_with_average.py`
- **Problem:** Replace missing (NaN) values in the sales column with the average sales value.
- **Concepts:** mean(), fillna(), handling missing data

---



### 6️⃣ Total Sales by Department (Pandas)
- **File:** `total_sales_by_department.py`
- **Problem:** Calculate total sales for each department.
- **Concepts:** groupby(), agg(), sum(), aggregation


---

### 7️⃣ Department with Highest Average Sales (Pandas)
- **File:** `department_with_highest_average_sales.py`
- **Problem:** Find the department that has the highest average sales.
- **Concepts:** groupby(), mean(), max(), idxmax()


---


### 8️⃣ Merge Employees with Bonus Data (Pandas)
- **File:** `merge_bonus_with_employees.py`
- **Problem:** Merge employee data with bonus percentage based on department, keeping all employees.
- **Concepts:** merge(), left join, joining DataFrames

---


### 9️⃣ Top 3 Employees with Highest Bonus (Pandas)
- **File:** `top3_employees_highest_bonus.py`
- **Problem:** Find the top 3 employees having the highest bonus amount.
- **Concepts:** merge(), new column creation, arithmetic operations, sort_values(), head()

---

### 🔟 High Value Customers (Pandas)
- **File:** `high_value_customers.py`
- **Problem:** Find customers who placed more than 2 orders and have total sales greater than 50000.
- **Concepts:** groupby(), agg(), filtering, multiple conditions, sorting

---

### 1️⃣1️⃣ Average Salary with Conditions (Pandas)
- **File:** `avg_salary_filtered_by_exp_salary.py`
- **Problem:** Find the average salary of each department for employees with salary > 50000 and experience >= 4, sorted by avg_salary descending.
- **Concepts:** filtering, multiple conditions, groupby(), mean(), sorting

---


### 1️⃣2️⃣ High Spending Delhi Customers (Pandas)
- **File:** `high_spending_delhi_customers.py`
- **Problem:** Find customers from Delhi whose total spending is greater than 10000, sorted by total spending.
- **Concepts:** merge(), filtering, groupby(), aggregation, sorting


---

### 1️⃣3️⃣ Employees Above Average Salary by City (Pandas)
- **File:** `employees_above_avg_salary_by_city.py`
- **Problem:** Count employees in each city whose salary is greater than the overall average salary.
- **Concepts:** mean(), filtering, groupby(), count(), aggregation

---
### 1️⃣4️⃣ City-wise Sales Summary (Pandas)
- **File:** `city_wise_sales_summary.py`
- **Problem:** For each city, find total amount, average amount, and count of completed orders.
- **Concepts:** groupby(), agg(), lambda function, conditional aggregation
---



### 1️⃣5️⃣ Top 2 Employees per Department (Pandas)
- **File:** `top2_employees_per_department.py`
- **Problem:** Rank employees by salary within each department and return top 2 highest paid employees.
- **Concepts:** groupby(), rank(), dense ranking, filtering, sorting

---


### 1️⃣6️⃣ Running Total Filter (Pandas)
- **File:** `running_total_filter.py`
- **Problem:** Calculate running total per customer and return rows where running total exceeds 4000.
- **Concepts:** sort_values(), groupby(), cumsum(), method chaining, filtering

---

### 1️⃣7️⃣ Rolling Average Sales Filter (Pandas)
- **File:** `rolling_average_sales.py`
- **Problem:** Calculate 3-day rolling average of sales and return rows where rolling average is greater than 300.
- **Concepts:** rolling(), mean(), time series, filtering


---

### 1️⃣8️⃣ Order Gap Analysis (Pandas)
- **File:** `order_gap_analysis.py`
- **Problem:** Calculate days difference between consecutive orders and return cases where gap is greater than 3 days.
- **Concepts:** merge(), sort_values(), groupby(), diff(), datetime operations

---

### 1️⃣9️⃣ Most Frequently Purchased Product per Customer (Pandas)
- **File:** `most_frequent_product_per_customer.py`
- **Problem:** Find the most frequently purchased product for each customer. If tie happens, choose product with higher total amount.
- **Concepts:** groupby(), aggregation, sorting, tie handling

---
### 2️⃣0️⃣ Employees Above Department Average Salary (Pandas)
- **File:** `employees_above_department_avg_salary.py`
- **Problem:** Find employees whose salary is greater than their department average salary.
- **Concepts:** groupby(), transform(), filtering, sorting

---

### 2️⃣1️⃣ Students Above Average Marks Threshold (Pandas)
- **File:** `students_above_average_marks.py`
- **Problem:** Find students whose average marks are greater than 70.
- **Concepts:** groupby(), aggregation, mean(), query()

---

### 2️⃣2️⃣ Product-wise Total Revenue (Pandas)
- **File:** `product_wise_total_revenue.py`
- **Problem:** Find total revenue generated by each product and sort by total revenue descending.
- **Concepts:** merge(), new column creation, groupby(), aggregation, sorting

---
### 2️⃣3️⃣ Customer Order Growth Analysis (Pandas)
- **File:** `customer_order_growth_analysis.py`
- **Problem:** Calculate previous order amount and percentage growth for each customer.
- **Concepts:** sort_values(), groupby(), shift(), percentage calculation

---

### 2️⃣4️⃣ Second Highest Salary by Department (Pandas)
- **File:** `second_highest_salary_by_department.py`
- **Problem:** Find the employee having the 2nd highest salary in each department.
- **Concepts:** groupby(), rank(), dense ranking, filtering


---
### 2️⃣5️⃣ Previous Month Sales (Pandas)
- **File:** `previous_month_sales.py`
- **Problem:** Create a previous month sales column using shift().
- **Concepts:** shift(), new column creation

---
### 2️⃣6️⃣ Store Sales Decrease Analysis (Pandas)
- **File:** `store_sales_decrease_analysis.py`
- **Problem:** Calculate month-over-month sales difference and find stores where sales decreased.
- **Concepts:** groupby(), diff(), filtering, time-based analysis

---
### 2️⃣7️⃣ Find Duplicate Transactions (Pandas)
- **File:** `find_duplicate_transactions.py`
- **Problem:** Find duplicate transactions based on same customer_id and amount.
- **Concepts:** duplicated(), filtering, duplicate detection

---

### 2️⃣8️⃣ Customers Without Orders (Pandas)
- **File:** `customers_without_orders.py`
- **Problem:** Find customers who never placed any order.
- **Concepts:** merge(), left join, isna(), filtering

---

### 2️⃣9️⃣ Highest Performance Employee by Department (Pandas)
- **File:** `highest_performance_employee_by_department.py`
- **Problem:** Find the employee with the highest performance score in each department.
- **Concepts:** groupby(), rank(), ranking, filtering
---
### 3️⃣0️⃣ Region Product Sales Pivot Table (Pandas)
- **File:** `region_product_sales_pivot.py`
- **Problem:** Create a pivot table with region as rows, product as columns, and total sales as values.
- **Concepts:** groupby(), sum(), unstack(), pivot_table()

---

### 3️⃣1️⃣ Latest Order per Customer (Pandas)
- **File:** `latest_order_per_customer.py`
- **Problem:** Find the latest order for each customer.
- **Concepts:** to_datetime(), sort_values(), groupby(), tail()


---

### 3️⃣2️⃣ Products Without Sales (Pandas)
- **File:** `products_without_sales.py`
- **Problem:** Find products that never appeared in the sales table.
- **Concepts:** merge(), left join, isna(), filtering

---

### 3️⃣3️⃣ Wide to Long Format Conversion (Pandas)
- **File:** `wide_to_long_format_conversion.py`
- **Problem:** Convert wide-format data into long-format using Pandas.
- **Concepts:** melt(), reshaping data, wide-to-long transformation

---

### 3️⃣4️⃣ Highest Salary Employee by Department (Pandas)
- **File:** `highest_salary_employee_by_department.py`
- **Problem:** Find the employee having maximum salary in each department.
- **Concepts:** groupby(), idxmax(), row selection


---

### 3️⃣5️⃣ Customer Spending by Category (Pandas)
- **File:** `customer_spending_by_category.py`
- **Problem:** Find customers spending more than 5000 in Electronics and more than 2000 in Clothing.
- **Concepts:** groupby(), sum(), unstack(), conditional filtering

---
### 3️⃣6️⃣ 3-Day Rolling Average (Pandas)
- **File:** `rolling_average_3days.py`
- **Problem:** Create a rolling_avg_3days column using current row and previous 2 rows average.
- **Concepts:** rolling(), mean(), rolling window calculations
