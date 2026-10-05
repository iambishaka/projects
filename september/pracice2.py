def calculate_bill(price,quantity):
    total = price * quantity

    discount = 10
    discount_amount = total * discount / 100

    total = total - discount_amount

    return total
     
price = float(input("Enter price:"))
quantity = int(input("Enter quantity:"))

bill = calculate_bill(price,quantity)

print("Total bill:",bill)


def check_temprature(temp):
    if temp >= 35:
        return "very hot"
    elif temp >= 25:
        return "warm"
    elif temp >=15:
        return "cool"
    else:
        return "cold"

temprature = float(input("Enter temprature:"))

print(check_temprature((temprature)))
       
