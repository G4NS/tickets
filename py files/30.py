list = []
n = 12 #ай
all = 0 #общ
arf = 0 #арифметикалык ортасы

for i in range(n):
    list.append(int(input(str(i+1) + ". ")))
    all += list[i]

print("Жалпы молшеры: " + str(all))

for i in range(n):
    buffer_list = 0
    buffer = 0
    while(buffer <= i):
        buffer_list += list[buffer]
        buffer += 1
    print(str(i + 1) + "-шы айдагы жауын-шашыннын орташа молшеры" + str(buffer_list / (i + 1)))

print("Жауын шашынын ен аз молшеры: " + str(min(list)))