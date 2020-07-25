import numpy
arr = list(map(int, input().split()))
arr = numpy.array(arr)
print(arr.reshape(3,3))
