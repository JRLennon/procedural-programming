while True:
    age = int(input("What is your age? "))
    try:
        if age <12 and age >=0:
            print("You can watch a children's film")
        elif age >=12 and age <=14:
            print("You can watch a 12+ film.")
        elif age >=15 and age <=17:
            print("You can watch a 15+ film.")
        elif age >=18:
            print("You can watch any age-rated film in this example.")
        else:
            print("Your age is invalid. Please try again")
    except Exception as e:
        print(f"Error calculating valid age range: {e}")