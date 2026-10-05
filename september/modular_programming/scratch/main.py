from features import greet,discount
from utils import isinteger

print(greet("Sudarshan"))

print(f"Amount after discount = {discount(2580)}")


age = input("Please enter your age : ")

if isinteger(age):
    print(f"Your age is : {age}")
else:
    print("Wrong input !")
