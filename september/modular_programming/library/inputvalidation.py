def validate_int(n):
    try:
        n = int(n)
        return [True, n, f"Valid input {n}"]    # numbers = [3,5,6], items = [23.56, 6, True]
    except Exception as e:
        return [False, e, f"Invalid input {n}"]

# x = input("Enter your age : ")

# print(validate_int(x)[1])
