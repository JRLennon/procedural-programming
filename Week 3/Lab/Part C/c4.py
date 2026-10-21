print("Travel Adviser")

weather = input("What are the current weather conditions? (sunny/rainy): ").strip().lower()

try:
    distance = float(input("Journey distance (in miles): "))
    budget= float(input("Available budget in GBP: "))

    if distance <=0 or budget <0:
        print("Please enter a distance above 0 miles, and a budget of £0 or higher.")
    elif weather not in ("sunny", "rainy"):
        print("Invalid weather - Ente reither 'sunny' or 'rainy'")
    elif distance <=1 and weather == "sunny":
        print("Recommendation: Take a walk - It is a short journey and the weather is suitable")
    elif weather == "rainy" and budget >=3:
        print("Recommendation: Take the bus - A single bus trip will cost you £3")
    elif distance <=3 and weather == "sunny":
        print("Recommendation: Walk if you feel comfortable; otherwise consider a bus.")
    else:
        taxi_cost = distance * 2 # random number, no basis in reality

        if budget >= taxi_cost:
            print(f"Recommendation: Take a taxi. It will cost £{taxi_cost:.2f}.")
        elif budget >= 3:
            print("Recommendation: Take the bus - A single bus trip will cost you £3")
        else:
            print("Your budget is too low for the bus or taxi. Consider walking if practical.")
except ValueError: # e.g. if the user types in gibberish characters
    print("Please enter the distance and budget as numbers.")