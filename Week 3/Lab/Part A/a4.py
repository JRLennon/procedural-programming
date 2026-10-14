mark = float(input("Enter a mark between 0 and 100: "))

if mark >=70 and mark <=100:
    print("First!")
elif mark >=60 and mark <=69:
    print("Upper Second")
elif mark >=50 and mark <=59:
    print("Lower Second")
elif mark >=40 and mark <=49:
    print("Pass")
elif mark <40 and mark >=0:
    print("Fail")
else:
    print(f"Invalid mark - The mark entered was {mark}") # invalid mark check was included to check if the data inputted is within the expected boundary of 0 and 100.
