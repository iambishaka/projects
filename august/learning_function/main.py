# you write function like this
def greet(name, gender):                # def keyword , then function name, then parameters
    if gender == 'f':
        return f"Hello, Ms. {name}"
    elif gender == 'm':
        return f"Hello, Mr. {name}"
    else:
        return f"Hello, {name}"     # onc you use return statement function will end there


# now to use the function , you need to call it  
# to call the function just write its name and pass the argument

print(greet("bishaka","f"))

print(greet("barun","m"))


def washing_machine(clothes, detergent, water):
    return f"Cothes {clothes}, cleaned with {detergent} and {water}"


result = washing_machine("Shirts", "Surf Excel", "water")

print(result)


def addition(a,b):
    return a+b

print(addition(67,89))

r = addition(454677, 23434)

print(r)

