list = []

for i in range(20):
    list.append(int(input(str(i + 1) + " = ")))

mmin = min(list)
mmax = max(list)

print("min = " + str(mmin) +"\nmax = " + str(mmax))