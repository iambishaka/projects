from inputvalidation import validate_int

n = input("Enter first number :")
m = input("Enter second number :")

def add(a,b):
    v1 = validate_int(a)        # [True, 10, message]
    v2 = validate_int(b)
    if v1[0] and v2[0] == True:
        return v1[1] + v2[1]
    else:
        return f"Please check inputs {a,b}"

print(add(m,n))

# def add(a,b):
#     if validate_int(a)[0] == True:
#         if validate_int(b)[0] == True:
#             return int(a)+int(b)

# print(add(m,n))

value1 = 10
value2 = "Twelve"

r1 = validate_int(value1)
r2 = validate_int(value2)


# print(r1[0])
# print(r2[0])
