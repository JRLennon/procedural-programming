not_divisible_by_3 = []

for i in range(0, 100):
    if (i % 3 != 0):
        not_divisible_by_3.append(i)

for i in range(len(not_divisible_by_3)):
    print(not_divisible_by_3[i])