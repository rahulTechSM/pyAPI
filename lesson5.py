import numpy as np

data = np.array([
[50,55,60],
[40,45,48],
[30,35,38]

])

print(data)

#print(np.sum(data))


print(np.sum(data,axis=1))