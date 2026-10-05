def is_even(num):
    """Returns True if num is even, False otherwise."""
    if num % 2 == 0:
        return True
    else:
        return False

# n1 =  4
# print(is_even(n1))

numbers = [11, 12, 13, 17, 19, 101, 3, 5, 15, 14, 77]

for i in numbers:
    # print(i, is_even(i))
    # print(f"{i} is Even : {is_even(i)}")
    if is_even(i):
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")




# def create_greeting(name):
#     """Combines a name into full sentence."""
#     return "Hello, " + name + "! Welcome to Python."
#
# print(create_greeting("Diksha"))
# message = create_greeting("Srijana")
# print(message)

# def double_number(num):
#     """Takes a number and returns it multiplied by 2."""
#     result = num * 2
#     return result
#
# n = double_number(5)
# print(n) # 10
#
# print(double_number(10)) # 20
#
# my_var = double_number(3)
#
# print(my_var + 1)


