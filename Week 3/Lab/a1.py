current_weather = input("What is the weather currently? ")

if current_weather.lower() == "sunny":
    print("Great! Go for a walk.")
elif current_weather.lower() == "rainy":
    print("Take an umbrella.")
elif current_weather.lower() == "snowy":
    print("Stay warm and be careful!")
else:
    print("I don't recognise that weather.")