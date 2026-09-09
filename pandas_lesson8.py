import pandas as pd

data = {
    "Employee": [
        " rahul srivastava ",
        "RAVI MISHRA",
        " neha ",
        "Amit Kumar"
    ],

    "Department": [
        "technical",
        "SALES",
        "hr",
        "Sales"
    ],

    "JoiningDate": [
        "2024-01-15",
        "2023-06-20",
        "2025-03-10",
        "2022-11-05"
    ],

    "Salary": [
        "30000",
        "25000",
        "22000",
        "35000"
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nData Types:")
print(df.dtypes)

print("\n handle dates")
df["JoiningDate"]=pd.to_datetime(df["JoiningDate"])

print(df)

print("\nData Types:")
print(df.dtypes)

df["JoiningYear"] = df["JoiningDate"].dt.year
print(df)
print("\nData Types:")
print(df.dtypes)


df["JoiningMonth"] = (
    df["JoiningDate"].dt.month
)
print(df)
print("\nData Types:")
print(df.dtypes)

df["MonthName"] = (
    df["JoiningDate"].dt.month_name()
)
print(df)
print("\nData Types:")
print(df.dtypes)


df["Date"] = (
    df["JoiningDate"].dt.day
)
print(df)
print("\nData Types:")
print(df.dtypes)


df["JoiningDayName"] = (
    df["JoiningDate"].dt.day_name()
)
print(df)
print("\nData Types:")
print(df.dtypes)


result = df[df["JoiningDate"].dt.year >2024]
print(result)


result = df[
    df["JoiningDate"].between(
        "2023-01-01",
        "2024-12-31"
    )
]

print("\nfilter between date:")


print(result)


