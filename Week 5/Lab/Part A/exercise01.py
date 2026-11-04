def calculate_profit(sales):
    return sales * 0.23

while True:
    print(f"Expected profit: {calculate_profit(float(input("Enter projected sales: ")))}")