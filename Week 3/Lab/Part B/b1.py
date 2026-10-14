age = int(input("What is your age? "))
height = int(input("What is your height, in centimetres? "))

if age <12:
    print("You are too young for this ride.")
elif age >=12 and height >=140:
    print("You can ride!")
elif age >=12 and height<140:
    print("You do not meet the height requirement.")
else:
    print(f"Error calculating validity - You entered an age of {age} and a height of {height} cm.")