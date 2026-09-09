import pandas as pd

data = {

"Employee" :[
    "Rahul",
    "Ravi Mishra",
    "Ramesh",
    "Neha"
],
"Salary":[
    10000,
    12000,
    8000,
    7000
],
"Sales":[
    10,
    40,
    30,
    20
]


}


df = pd.DataFrame(data)
df["Target"] =30
print(df)


def performance(sales):

    if(sales >30):
        return "very good"
    elif(sales >=20):
        return "ok"
    else:
        return "bad"

df["Status"] = df["Sales"].apply(performance)


print(df)
