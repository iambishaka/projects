def calculate_total(price, quantity):       # we use 'def' to define a function, function takes some values ( price, quantity)
    total = price * quantity                # it proccesses the value
    return total                            # then returns it

# how do we use function ?

# p = 499
# q = 2
#
# amt = calculate_total(p,q)
# print(f"Total Amount : {amt}")  # this is new syntax
# print("Total Amount :", amt)    # this is the old way
#
# another_item_price = 185.00
# another_item_quantity = 5
# t = calculate_total(another_item_price,another_item_quantity)
# print(f"Total Amount : {t}")

def calculate_discount(amount, discount_percent):
    discount = (amount * discount_percent)/100
    discounted_price = amount - discount
    return discounted_price

# amount = 20000
# less = 10
#
# final_price = calculate_discount(amount,less)
# print(f"Please pay : {final_price}")
#
# a = float(input("Amount : "))
# d = int(input("Discount : "))
#
# print(f"Final Price : {calculate_discount(a,d)}")
#

def celsius_to_fahrenheit(c):
    f = (c*(9/5))+35
    return f

# print(celsius_to_fahrenheit(37))

def is_adult(age):
    return age>=18

# age = 11
#
# if is_adult(age):
#     print("Access granted!")
# else:
#     print("Access denied!")

def clean_name(name):
    name = name.strip()
    name = name.title()
    return name

user = "     rahul       "
# print(clean_name(user))

def validate_email(email):
    if "@" in email and "." in email:
        return True

    return False

print(validate_email("dfafasfasfas"))
print(validate_email("alex123@hotmail.com"))
print(validate_email("alex123.com"))
print(validate_email("alex445@"))
