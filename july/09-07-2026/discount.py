name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

print("------- MOVIE DISCOUNT --------")

if age <12:
    print(f"Hi{name.capitalize()}, discount applied")
elif age>12:
    print(f"Hi {name.capitalize()},discount not applied")
