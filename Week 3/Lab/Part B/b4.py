def calc_discount(total, student):
    if total <0:
        discount = -1
    if total <50:
        discount = 0.0 # No discount provided
    elif total  >=50 and total <100:
        discount = 0.10 # 10% discount
    elif total >=100:
        discount = 0.20 # 20% discount

    # additional discount if student
    if student:
        discount = discount + 0.05

    return(discount)
        

def shopping_valid(total):
    if total <0:
        print("Invalid shopping amount")
        return False
    else:
        return True
while True:
    shopping_total = float(input("What is the total amount of your shopping? "))
    student = input("Are you a student? (Y/N)")

    if student.lower() == "y":
        student = True
    else:
        student = False

    if shopping_valid(shopping_total):
        print(f"Original amount: £{shopping_total:.2f}")
        discount = (calc_discount(shopping_total, student) * shopping_total) if shopping_valid(shopping_total) else None
        print(f"Discount: £{discount:.2f}") if shopping_valid(shopping_total) else None
        print(f"Final amount: £{shopping_total - discount:.2f}") if discount else None
    else:
        break