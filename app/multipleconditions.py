import numpy as np

# array 0-attendance 1-salary 2- eperience

sales = np.array([
    [95,5000,2],
    [90,5500,3],
    [93,5000,2],
    [80,4000,2],
    [85,4500,2]
    ])

#print(sales)

salaries = sales[:,1]

attendance = sales[:,0]

#print(salaries)
#print(attendance)

result = sales[(salaries >= 5000) & (attendance >=85)]

print(result)


#max salaries index

maxsalaryindex = np.argmax(salaries);
print(maxsalaryindex);