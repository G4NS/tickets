import random
from array import *

n = 25
arr = array("i", [])

for i in range(n):
    arr.insert(i, random.randint(1, 99))
print(arr)

for i in range(n - 1):
    for j in range(n - i - 1):
        if(arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)