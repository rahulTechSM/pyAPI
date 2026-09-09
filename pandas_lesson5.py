import pandas as pd
import numpy as np

data = {
    "Employee": [
        " Rahul ",
        "Ravi",
        "Rohit",
        "Neha",
        "Amit",
        "Ravi"
    ],

    "Department": [
        "Technical",
        "Tech",
        "Sales",
        np.nan,
        "Sales",
        "Tech"
    ],

    "Salary": [
        10000,
        15000,
        12000,
        np.nan,
        18000,
        15000
    ]
}

df = pd.DataFrame(data)

print("===== ORIGINAL =====")
print(df)


# Remove spaces
df["Employee"] = (
    df["Employee"].str.strip()
)


# Standardize department
df["Department"] = (
    df["Department"].replace(
        "Tech",
        "Technical"
    )
)


# Fill department
df["Department"] = (
    df["Department"].fillna("Unknown")
)


# Calculate average salary
average_salary = df["Salary"].mean()


# Fill missing salary
df["Salary"] = (
    df["Salary"].fillna(average_salary)
)


# Convert salary
df["Salary"] = (
    df["Salary"].astype(int)
)


# Remove duplicates
df.drop_duplicates(
    inplace=True
)


# Reset indexes
df.reset_index(
    drop=True,
    inplace=True
)


print("\n===== CLEAN DATA =====")
print(df)