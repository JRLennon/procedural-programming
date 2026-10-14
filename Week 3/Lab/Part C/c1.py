def eligibility_checker(age: int, total: float, status: bool, discount: bool):
    if total <=0:
        print("Invalid order total.")
        order_status = 0
        return 0
    elif account_status == False:
        print("Please activate your account.")
        order_status = 0
        return 0

    if age >=18 and total <=500:
        print("Order approved.")
        order_status = 1 # Approved
    elif age >=18 and total >500:
        print("Additional verification required.")
        order_status = 0
        return 0
    elif age <18 and total <100:
        parent_authorised = input("Do you have parental authorisation (yes/no): ")
        if parent_authorised.lower() == "yes":
            print("Order approved.")
            order_status = 1 # Approved
        else:
            print("Order denied.")
            order_status = 0
            return 0

    # by this point, if the order wasn't approved, it would have already returned 0, and thus broken out of the loop.
    if order_status == 1: # If the order was approved
        if status == True and discount == True:
            print(f"You have been given a 10 percent discount. Your order of £{total:.2f} has been reduced to £{total*0.9:.2f}") # 10% discount, so 90% of the cost
            return 1 # order valid, there is a valid discount & it has been applied.
        elif status == True and discount == False:
            print(f"You do not have any valid discounts. Your order is £{total:.2f}")
            return 1 # order valid, but no discount
    elif order_status == 0: # If the order was not approved.
        print("Your order was not approved.") # It shouldn't ever get to here, should exit above.
        return 0


while True:
    try:
        # take user inputs
        age = int(input("Age: "))
        order_total = float(input("Order Total: "))
        account_status = input("Account Status (yes/no): ")
        valid_discount_code = input("Valid Discount Code (yes/no): ")

        status = False
        # parsing inputs
        if account_status.lower() == "yes":
            status = True
        else:
            status == False
        if valid_discount_code.lower() == "yes":
            discount = True
        else:
            discount = False

        eligble = eligibility_checker(age, order_total, status, discount)
        if eligble == 0:
            break # break out of the while loop
    except Exception as e:
        print(f"Error occured: {e}")
