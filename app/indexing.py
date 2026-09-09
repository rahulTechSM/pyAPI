import numpy as np

employees = np.array([
                    [95,10000,2],
                    [90,10000,3],
                    [80,8000,1]

])

#all employee
print(employees)
#indexing
print(employees[0]) 
print(employees[2,1]) 
#negative indexing
print(employees[-1])

#selecting coloums

print(employees[:,1])
#Slicing Rows
print(employees[1:2])
print(employees[:,0:2])