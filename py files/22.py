list = []
all = 0

for i in range(15):
    list.append(input(str(i + 1) + ". "))
    all += int(list[i])

print("Косындысы: " + str(all) + "\nАрф. Ортасы: " + str(int(all) / 15))

