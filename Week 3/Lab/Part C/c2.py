balance = 1000.0
pin = 1234

while True:
    try:
        input_pin = input("PIN: ")
        if int(input_pin) != pin:
            print("Incorrect PIN!")
            break
        
        user_action = input("Please choose an action (balance, withdraw, deposit): ") # If the pin is not correct, it's valid. Ask for options.
        
        if user_action.lower() == "balance":
            print(f"Your current balance is {balance:.2f}")
        elif user_action.lower() == "withdraw":
            withdraw_amount = float(input("Withdrawal amount: "))
            if withdraw_amount >0 and withdraw_amount < balance:
                balance = balance - withdraw_amount
                print(f"You have withdrawn £{withdraw_amount:.2f} from your account. Your balance now stands at {balance}.")
            else:
                print(f"Cannot withdraw {withdraw_amount} from account. Your balance stays at {balance}.")
        elif user_action.lower() == "deposit":
            deposit_amount = float(input("Deposit amount: "))
            if deposit_amount >0:
                balance = balance + deposit_amount
                print(f"You have deposited £{deposit_amount:.2f} into your account. Your balance now stands at {balance}.")
            else:
                print(f"Cannot deposit {deposit_amount} into account. Your balance stays at {balance}.")
        else:
            print("Invalid menu choice. The options are 'balance', 'withdraw' or 'deposit' - Please try again.")
    except Exception as e:
        print(f"Error occured: {e}")