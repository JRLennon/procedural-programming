number = 0
for i in range(2000, 3000): # 2000 to 2999
    if (i % 13 == 0):
        number += 1
        if number == 2:
            print(i) # should return 2015: this is the second divisible number by 13 in the range 2000 to 2999