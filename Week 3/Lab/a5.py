while True:
    name = input("What is your name? ")
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Your age is invalid.")
        break
    fav_programming_language = input("What is your favourite programming language? ")

    print(f"Hello, {name.title()}")

    if age <18 and age >=0:
        print("You are still learning and developing your skills.")
    elif age >=18:
        print("Keep developing your programming skills!")
    else:
        print(f"Your age of {age} is invalid.")
    
    if fav_programming_language.lower == "python": # This is done in an a separate if statement - If it was done through an elif statement in the above block, it might not run.
        print("Python is a great language to learn!")