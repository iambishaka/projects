name = input("Enter your name : ")
age = int(input("Enter your age"))

print("----- Annapurna Bhandar --------")

if age<25:
    print(f"Hello {name.capitalize()}, you are under age for this scheme.")
elif age>60:
    print(f"Hello {name.capitalize()}, you are over age for this scheme.")
else:
    print(f"Hello {name.capitalize()}, you are eligible for this scheme.")


