# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats
i = 0
arr = []
n = int(input(''))
arr = list(map(int, input().split()))
arr.sort()
x = np.mean(arr)
y = np.median(arr)
z = stats.mode(arr)
print(round(x,1))
print(round(y,1))
print('%d' %(z[0]))