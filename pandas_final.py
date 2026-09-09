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

df["Employee"] = df["Employee"].str.strip()
df["Employee"] = df["Employee"].str.title()
df["Employee"] = df["Employee"].str.upper()
df["Employee"] = df["Employee"].str.lower()

result = df[df["Employee"].str.contains(
 "ravi",
 case=False

)]


result = df[df["Employee"].str.startswith(
 "R",
 
 

)]
print(result)

currenttimeDate = pd.Timestamp.now()

print(currenttimeDate)
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])
df["noofworkingdays"] = (currenttimeDate-df["JoiningDate"]).dt.days



print(df)