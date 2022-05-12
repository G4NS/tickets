import random
from array import *

arr = array("i", [])
n = 18
for i in range(n):
    arr.insert(i, random.randint(1, 99))

print(*arr)

index = 0
minindex = 0


while index < n-1:
    minindex = index
    j = index + 1
    while j < n:
        if arr[j] < arr[minindex]:
            minindex = j
        j += 1

    arr[index], arr[minindex] = arr[minindex], arr[index]
    index += 1

print(*arr)
