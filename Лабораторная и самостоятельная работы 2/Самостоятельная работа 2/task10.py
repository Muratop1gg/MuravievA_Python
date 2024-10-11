list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

div2 = 0

notdiv2 = 0

for i in list_:
    if i % 2 == 0:
        div2 += 1
    else:
        notdiv2 += 1

if div2 > notdiv2:
    print("Четных чисел больше")
else:
    print("Нечетных  чисел больше")