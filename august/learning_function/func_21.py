def add(a,b,c):       # parameters (a,b)
    return a+b+c


r = add(55,65,35)      # arguments (55,65)
# print(r)

# TYPE HINTS (declaring the variable and rturn type)
def user_detector(age:int) -> str | None:     # 1 parameter, integer
    if age < 18:            # if age is below 18
        return "Child"      # it will return a string "Child"
    if age >= 18:
        return "Adult"

a = user_detector(20)
# print(a)

age = "twenty one"


def age_verify(age:int,name:str) -> str:
    if age > 40:
        return f"Sorry {name}, you are over aged for paragliding"
    if 18 <= age <= 40:
        return f"Welcome {name}, you can go for paragliding"
    if age < 18:
        return f"Sorry {name}, you are under age for paragliding"

    return "Error occurred"


l = age_verify(-71,"Aryan")
# print(l)



def greet(name:str="Student") -> str:
    return f"Hello {name.title()}!"

print(greet("barun"))
print(greet("bishaka"))
print(greet())
print(greet("ravi"))
print(greet("neha"))
print(greet())

def welcome(name="Guest"):                  # default parameter value
    return f"Welcome to our website, {name}"

print(welcome("Barun"))
print(welcome())                            # if value is not passed, default value will be used

def calc_gst(amount:float, gst:int=18) -> float:
    return amount+(amount*(gst/100)) 

print(calc_gst(100, 12))
print(calc_gst(200))
