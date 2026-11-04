def calculate_average(temperatures):
    return sum(temperatures) / len(temperatures)

def find_highest(temperatures):
    return max(temperatures)

def find_lowest(temperatures):
    return min(temperatures)

def count_hot_days(temperatures):
    hot_days = 0
    for i in temperatures:
        if i >20:
            hot_days +=1
    return hot_days
        

temperatures = [12, 15, 18, 21, 19, 16, 14, 11]

print(f"Average temperature: {calculate_average(temperatures)}")
print(f"Highest temperature: {find_highest(temperatures)}")
print(f"Lowest temperature: {find_lowest(temperatures)}")
print(f"Number of hot days: {count_hot_days(temperatures)}")


