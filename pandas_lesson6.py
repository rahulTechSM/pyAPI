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


#values count
count = df["Status"].value_counts()
#print(count)

common = df["Status"].unique()
#print(common)


#group by
SalesPerEmployee = df.groupby("Employee")["Sales"].sum()

#print(SalesPerEmployee)

#avg sales by employee

avgSalesPerEmployee = df.groupby("Employee")["Sales"].mean().round(2)

#print("/n avg sales /n")
#print(avgSalesPerEmployee)


#Aggregation all operation to gether

result =( 
df.groupby("Employee")["Sales"].agg(["sum","mean","max","min"])
)
result.rename(

    columns={
        "Sum" :"total sales"
    },
    inplace=True
)
#print(result)

#multiple group by
print(df.groupby(["Bank","Employee"])["Sales"].sum())

#group by with filter

approved = df[
    df["Status"] == "Approved"
]
print(approved)

result1 = approved.groupby(["Employee","Product"])["Sales"].sum()
result1 = result1.sort_values(
   
    ascending=False
)

print(result1)


report2 = (
    df.groupby("Employee")
    .agg(
        TotalSales=("Sales", "sum"),
        AvgSales=("Sales", "mean"),
        Applications=("Sales", "count")
    ).round(2)
    .reset_index()
)

print(report2.to_string(index=False))