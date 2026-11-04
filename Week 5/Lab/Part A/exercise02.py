def calculate_fuel_cost(distance, mpg, price_per_litre):
    gallons_used = distance / mpg
    litres_used = gallons_used * 4.546
    return litres_used * price_per_litre

distance = float(input("Enter journey distance (miles): "))
mpg = int(input("Enter car fuel efficiency (MPG): "))
price_per_litre = float(input("Enter petrol price per litre (£): "))

cost = calculate_fuel_cost(distance, mpg, price_per_litre)
print(f"Estimated fuel cost: £{cost:.2f}")

