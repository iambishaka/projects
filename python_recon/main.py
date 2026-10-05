# def next_year():
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))
#
#     print(f"Hi {name} you will turn {age+1} next year.")
#
# # DRY = Don't Repeat yourself
#
#
# next_year()
# next_year()
# next_year()
# next_year()
# next_year()
# next_year()

name_1 = 'alex'             # Global

def addition():
    name_2 = 'john'         # scoped
    print(name_2)
    x = int(input("Enter a number : "))
    y = int(input("Enter another number : "))
    total = x + y
    print(f"Sum of {x} and {y} = {total}")

print(name_1)

# addition()
