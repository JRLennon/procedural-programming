loan_amount = float(input("Enter the total loan amount (£): "))
annual_rate = float(input("Enter the annual interest rate (%): "))
years = float(input("Enter the repayment period (years): "))

if loan_amount <=0 or years <=0:
    print("Invalid input.")
else:
    months = years * 12

    if annual_rate == 0:
        monthly_payment = loan_amount / months
    elif annual_rate > 0:
        monthly_rate = annual_rate / 100 / 12

        # M = P x r x ((1 + r) ** n) / (((1 + r) ** n) -1)
        monthly_payment = (
            loan_amount
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months -1)
        )
    else:
        print("Invalid interest rate.")
        monthly_payment = None

    if monthly_payment is not None:
        total_repaid = monthly_payment * months
        total_interest = total_repaid - loan_amount

        print(f"Monthly payment: £{monthly_payment:.2f}")
        print(f"Total amount repaid: £{total_repaid:.2f}")
        print(f"Total interest: £{total_interest:.2f}")

        if monthly_payment > 500:
            print("Warning: Your monthly payments are high.")

        if total_interest > loan_amount * 0.25:
            print("Warning: Your total interest is more than 25% of the original loan amount.")