import numpy as np
x, y, z = map(int, input().strip().split())
arr = np.array(input().strip().split(), int)
for j in range(1, x + y):
    arr = np.vstack((arr, np.array(input().strip().split(), int)))
print(arr)
