import pandas as pd


data = {
    "Employee": [
        "Rahul",
        "Ravi",
        "Rohit",
        "Neha",
        "Amit"
    ],

    "Department": [
        "Technical",
        "Technical",
        "Sales",
        "HR",
        "Sales"
    ],

    "Sales": [
        10,
        20,
        30,
        50,
        40
    ],

    "Salary": [
        10000,
        15000,
        12000,
        8000,
        18000
    ]
}

df = pd.DataFrame(data)

print(df["Sales"])

print(
    df[["Sales","Employee"]]
    )

print(df["Salary"]>10000)

result = df[df["Salary"] >10000]

print(result);


result1 = df[ (df["Salary"] >10000) & (df["Department"] == "Technical")]

print(result1)

print("\nloc:\n")

print(df.loc[0])

print("\n conditions loc :\n")

result2 = df.loc[
    df["Salary"] > 10000,
    ["Employee","Sales"]
]

print(result2)
print("=====================")
print(df.iloc[0])

print("=============sorting==========")

print(df.sort_values(
    by="Salary"
))


result11 = df.sort_values(
    by="Salary",
    ascending=False
)

print(result11)