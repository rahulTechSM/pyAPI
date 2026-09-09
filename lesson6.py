import numpy as np

sales = np.array([20000,30000,40000,50000,8000,9000])

target = 10000

#result = np.where(sales > target)

result = np.where(sales > target,"good","bad")
print(result)


salary = np.array([10000,2000,3000,5000,6000]);



result = np.where(salary > 5000)

print(result)