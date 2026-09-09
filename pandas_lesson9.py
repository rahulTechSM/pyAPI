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

#print(df.to_string(index=False))

result = pd.pivot_table(df,values="Sales",index="Employee",columns="Bank",aggfunc=sum)

print(result)


result = pd.pivot_table(df,values="Sales",index="Employee",columns="Bank",aggfunc=sum, fill_value=0,
    margins=True,margins_name="Total")
print(result)


result1 = pd.pivot_table(df,values="Sales",index="Bank",columns="Product",aggfunc=sum, fill_value=0,
    margins=True,margins_name="Total")
print(result1)


#multiple index

result2 = pd.pivot_table(df,values="Sales",index=["Bank","Product"],aggfunc=sum)

print(result2)


result3 = pd.pivot_table(df,values="Sales",index=["Bank","Employee"],columns="Product",aggfunc=sum)
result3 = result3.fillna(0)
print(result3)


result4 = pd.pivot_table(df,values="Sales",index=["Bank","Employee"],columns="Product",aggfunc=sum,fill_value=0)

print(result4)
