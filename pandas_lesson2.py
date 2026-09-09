import pandas as pd

data = {
    "Employees" :[
                "Rahul",
                "Ravi Mishra",
                "Rohit",
                "Neha"
                ],
                
    "Sales" :   [
            10,
            20,
            30,
            50

    ],

    "salary" : [
        10000,
        10000,
        12000,
        8000
    ]

}


df = pd.DataFrame(data)

#print(df)
#print("\nShape:")
#print(df.shape)
print(df["Employees"]);