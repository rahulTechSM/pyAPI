import numpy as np



employees = np.array([
    [95, 130, 5, 90],
    [80,  70, 2, 65],
    [98, 160, 7, 95],
    [90, 105, 3, 80],
    [85,  95, 4, 75]
])
#output demission of maritx rowsXcoloums 5x4
print(employees.shape)

rows = employees.shape[0]
columns = employees.shape[1]

print("Employees:", rows)
print("Features:", columns)