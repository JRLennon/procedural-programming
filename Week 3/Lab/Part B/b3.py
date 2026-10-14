correct_username = "student"
correct_password = "python123"

input_user = input("Username: ")
input_password = input("Password: ")

if (input_user == correct_username) and (input_password == correct_password):
    print("Login successful!")

    # age verification
    user_age = int(input("What is your age? "))
    print("Access granted.") if user_age >=18 else print("You must be at least 18.")
elif (input_user == correct_username):
    print("Username recognised.")
else:
    print("Incorrect username or password.")
