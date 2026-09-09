import pandas as pd

employees = {
    "EmployeeID": [101, 102, 103, 104],
    "Employee": ["Rahul", "Ravi", "Neha", "Amit"],
    "Department": ["Technical", "Sales", "HR", "Sales"]
}

sales = {
    "EmployeeID": [101, 102, 102, 104, 105],
    "Sales": [10, 20, 30, 40, 50]
}

employee_df = pd.DataFrame(employees)
sales_df = pd.DataFrame(sales)

print("EMPLOYEE MASTER")
print(employee_df)

print("\nSALES")
print(sales_df)


result = pd.merge(employee_df,sales_df,on="EmployeeID")

print("\n merge")
print(result)

print("\n InnerJoin")

result1 = pd.merge(employee_df,sales_df,on="EmployeeID",how="inner")

print(result1)

print("\n leftjoin")

result2 = pd.merge(employee_df,sales_df,on="EmployeeID",how="left")

print(result2)


print("\n handle nan")

result2["Sales"] = result2["Sales"].fillna(0)
print(result2)

print("\n outer join")



result3 = pd.merge(employee_df,sales_df,on="EmployeeID",how="outer")
print(result3)


employees = {
    "EmployeeID": [101, 102, 103, 104],
    "Employee": ["Rahul", "Ravi", "Neha", "Amit"],
    "Department": ["Technical", "Sales", "HR", "Sales"]
}

sales = {
    "emp_id": [101, 102, 102, 104, 105],
    "Sales": [10, 20, 30, 40, 50]
}
employee_df = pd.DataFrame(employees)
sales_df = pd.DataFrame(sales)
print("\n different column name")
result4 = pd.merge(employee_df,sales_df,left_on="EmployeeID",right_on="emp_id")


print(result4)
print("\n new")

employee_df = pd.DataFrame({
    "EmployeeID": [101, 102],
    "Employee": ["Rahul", "Ravi"],
    "Department": ["Technical", "Sales"]
})

sales_df = pd.DataFrame({
    "EmployeeID": [101, 102],
    "Department": ["Tech", "Sales"],
    "Sales": [10, 20]
})

result5 = pd.merge(
    employee_df,
    sales_df,
    on="EmployeeID",
    suffixes=(
        "_Master",
        "_Sales"
    )
)

print(result5)


print("\n concat")

jan = pd.DataFrame({
    "Employee": ["Rahul", "Ravi"],
    "Sales": [20, 30]
})

feb = pd.DataFrame({
    "Employee": ["Rahul", "Ravi"],
    "Sales": [25, 35]
})

result = pd.concat([jan,feb])

print(result)

result = pd.concat([jan,feb],ignore_index=True)
print(result)

