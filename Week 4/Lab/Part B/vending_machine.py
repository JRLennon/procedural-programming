balance = 200

print("Welcome to the Vending Machine!")

while True:
    print(f"Your balance is {balance}p")
    print("Please select an item:\n1. Crisps - 100p\n2. Chocolate - 150p\n3. Water - 120p\n4. Quit")

    selection = input("Please select an option: ")

    if selection.lower() == "crisps" or selection.lower() == "1":
        print("Purchase successful! You have purchased Crisps for 100p.")
        if balance >= 100:
            balance -= 100
        else:
            print("Insufficient balance for Crisps.")
    elif selection.lower() == "chocolate" or selection.lower() == "2":
        print("Purchase successful! You have purchased Chocolate for 150p.")
        if balance >= 150:
            balance -= 150
        else:
            print("Insufficient balance for Chocolate.")
    elif selection.lower() == "water" or selection.lower() == "3":
        print("Purchase successful! You have purchased Water for 120p.")
        if balance >= 120:
            balance -= 120
        else:
            print("Insufficient balance for Water.")
    elif selection.lower() == "quit" or selection.lower() == "4":
        print("Thank you for using the Vending Machine!")
        break
    else:
        print("Invalid selection. Please try again.")
