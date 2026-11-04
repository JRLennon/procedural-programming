num = int(input("Height: "))

def pyramid(num):
    for i in range(num):
        print(("*" * (i * 2 + 1)).center(num * 2 - 1))

print(pyramid(num))