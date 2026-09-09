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

print("\n employee data")
print(employee_df)

print("\n sales data")
print(sales_df)


result = pd.merge(
    employee_df,
    sales_df,
    on="EmployeeID"
    )


print("\n marge")
print(result)


result = pd.merge(
    employee_df,
    sales_df,
    on="EmployeeID",
    how="inner"
    )


print("\n marge")
print(result)

resultleft = pd.merge(
    employee_df,
    sales_df,
    on="EmployeeID",
    how="left"
    )
print("\n margeLeft")
print(resultleft)

resultleft["Sales"] = resultleft["Sales"].fillna(0)

print("\n margeLeft")
print(resultleft)


resultright = pd.merge(
    employee_df,
    sales_df,
    on="EmployeeID",
    how="right"
    )

print("\n margeright")
print(resultright)



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

resultnew = pd.merge(employee_df,sales_df,left_on="EmployeeID",right_on="emp_id")
print("\n inner")
print(resultnew)



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




resultnew1 = pd.merge(employee_df,sales_df,on="EmployeeID",suffixes=["_masterEmployee","_childSales"])
print("\n department columns name same")
print(resultnew1)



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

