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


print(df.dtypes)

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

print("\n inner")
print(df)


print(df.dtypes)

df["JoiningYear"] = df["JoiningDate"].dt.year

print("\n year")
print(df)


df["month"] = df["JoiningDate"].dt.month

print("\n month")
print(df)


df["monthName"] = df["JoiningDate"].dt.month_name()

print("\n monthName")
print(df)


df["day"] = df["JoiningDate"].dt.day

print("\n day")
print(df)



df["dayName"] = df["JoiningDate"].dt.day_name()

print("\n dayName")
print(df)


result = df[df["JoiningYear"] >2023]

print(result)


resultname = df[df["dayName"] =="Monday"]

print(resultname)

print("\n salary")

print(df.dtypes)


df["Salary"]= df["Salary"].astype(int)


print("\n salary")

print(df.dtypes)

df["SalaryAvg"] = df["Salary"].mean()

df["SalaryMax"] = df["Salary"].max()

df["SalaryMin"] = df["Salary"].min()

print(df)


#difference

reference = pd.Timestamp.now()

print(reference)

df["numberofDaysworked"]  = (reference - df["JoiningDate"]).dt.days

print(df)


df["Employee"] = (
    df["Employee"].str.strip()
)
print(df)

#Make names professional
df["Employee"] = (
    df["Employee"].str.title()
)

print(df)


df["Department"] = (
    df["Department"].str.upper()
)

print(df)


df["Department"] = (
    df["Department"].str.lower()
)
print(df)


result = df[
    df["Employee"].str.contains(
        "Ravi"
    )
]

print(result)


result = df[
    df["Employee"].str.contains(
        "ravi",
        case=False

    )
]
print(result)

result = df[
    df["Employee"].str.startswith("R")
]

print(result)

result = df[
    df["Employee"].str.endswith("Kumar")
]

print(result)

df["Department"] = (
    df["Department"]
    .str.replace(
        " Department",
        "",
        regex=False
    )
)

print(result)
