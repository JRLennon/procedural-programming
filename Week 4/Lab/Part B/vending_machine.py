balance = 200

print("Welcome to the Vending Machine!")
print(f"Your balance is {balance}p")

while True:
    print("Please select an item:\n1. Crisps - 100p\n2. Chocolate - 150p\n3. Water - 120p\n4. Quit")

    selection = input("Please select an option: ")

    if selection.lower() == "crisps":
        print("Purchase successful! You have purchased Crisps for 100p.")
        balance -= 100
    elif selection.lower() == "chocolate":
        print("Purchase successful! You have purchased Chocolate for 150p.")
        balance -= 150
    elif selection.lower() == "water":
        print("Purchase successful! You have purchased Water for 120p.")
        balance -= 120
    elif selection.lower() == "quit":
        print("Thank you for using the Vending Machine!")
        break
    else:
        print("Invalid selection. Please try again.")
