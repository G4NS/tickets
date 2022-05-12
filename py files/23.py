from array import *

n = int(input("n = "))
buffer = 0
all = 0
arr = array("i", [])

for i in range(n):
    arr.insert(i, int(input(str(i+1) + ". ")))

buffer_max = arr[0]

for i in range(n):
    if(buffer_max <= arr[i]):
        buffer_max = arr[i]
        buffer = i

buffer += 1
while(buffer < n):
    all += arr[buffer]
    buffer += 1

print("Ен улкен элемент: " + str(buffer_max))
print("Косындысы: " + str(all))