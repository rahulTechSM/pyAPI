import pandas as pd

data = {
    "Employee": [
        "Rahul",
        "Ravi",
        "Rahul",
        "Neha",
        "Ravi",
        "Rahul",
        "Neha",
        "Ravi"
    ],

    "Bank": [
        "DIB",
        "FAB",
        "DIB",
        "FAB",
        "DIB",
        "FAB",
        "DIB",
        "FAB"
    ],

    "Product": [
        "Card",
        "Loan",
        "Loan",
        "Card",
        "Card",
        "Loan",
        "Loan",
        "Card"
    ],

    "Sales": [
        10,
        20,
        30,
        15,
        25,
        40,
        20,
        30
    ],

    "Status": [
        "Approved",
        "Pending",
        "Approved",
        "Rejected",
        "Approved",
        "Approved",
        "Pending",
        "Approved"
    ]
}

df = pd.DataFrame(data)
print(df)
result = pd.pivot_table(df,values="Sales",index="Bank",aggfunc=sum)
print(result)
result1 = pd.pivot_table(df,values="Sales",index="Bank",columns="Employee",aggfunc=sum,margins=True,margins_name="Total Cards")

print(result1)


result2 = pd.pivot_table(df,values="Sales",index=["Bank","Employee"],columns="Product",aggfunc=sum,margins=True,margins_name="Total Sales",fill_value=0)
print("\n")
print(result2)