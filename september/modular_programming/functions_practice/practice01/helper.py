    from datetime import datetime

# in the world of programming this concept is called Encapsulation
def greet(name, gender, married):
    s = "Mr."
    t = "Hello"
    h = datetime.now().hour
    # print(h)   # debugging 
    if h < 12:
        t = "Good Morning"
    if h < 16 and h > 12:
        t = "Good Afternoon"
    if h >= 16:
        t = "Good Evening"

    if married == None:
        married = False

    if gender == "Female" and married == True:
        s = "Mrs."

    if gender == "Female" and married == False:
        s = "Miss"

    message = f"{t} {s} {name.title()}"
    return message
