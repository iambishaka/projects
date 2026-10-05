bill = float(input("Enter the total bill : "))

if bill >= 2000:
    print(f"you got 20% off",) 
    print(f"after the discount  {bill - (bill* 0.2)}")

elif 1000 <= bill <= 2000:
    print("you got 10% off")
    print(f"final amount {bill - (bill * 0.1)}")
 
else: 
    print(f"Final amount = {bill}")
