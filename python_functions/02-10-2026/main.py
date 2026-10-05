# ======= FUNCTION UNDERSTANDING EVALUATION ========
#1
def double_number(a):
    return a * 2

result = double_number(6)
print(result) # 10

#2
def add_number(a,b):
    return a + b

total = add_number(7, 6)
print(total) # 13

#3
def check_even_odd(a):
    if a == 0:
        return "INVALID INPUT"

    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"



print(check_even_odd(4)) # Even
print(check_even_odd(7)) # Odd


