import random
from array import *

n = 20
arr = array("i", [])
for i in range(n):
    arr.append(random.randint(1, 99))
print(*arr)

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    elem =arr[0]
    left = list(filter(lambda x: x < elem, arr))
    center = [i for i in arr if i == elem]
    right = list(filter(lambda x: x > elem, arr))

    return quick_sort(left) + center + quick_sort(right)

print(*quick_sort(arr))