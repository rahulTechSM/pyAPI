import numpy as np
import pandas as pd

sales = pd.Series([
    50000,
    80000,
    120000,
    150000
])

#print(sales)

sales = pd.Series(
    [50000,20000,40000],
    index = ["r","h","L"]
)

print(sales)