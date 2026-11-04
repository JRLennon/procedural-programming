import math

def calculate_area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(
        semi_perimeter
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )
    return area

print(calculate_area(3, 4, 5))
print(round(calculate_area(7, 8, 9), 2))

# following test cases, it should return 6.0 and 26.83.