# parameters
# Name _______ Age ____ Gender ____ <-------- Parameter
# Name Bishaka Age 19 Gender Female <-------- Arguments

# def greet():
#     return "Welcome to class"
#
# print(greet())

# ------- THIS IS OUT FUNCTION --------
# it takes a name and returns a welcome message
def welcome_students(student_name):
    return f"Welcome to class, {student_name}"

# this is out data
students = [ 'neha', 'alam', 'jasmine', 'roza', 'sameer', 'dakshita', 'jiya', 'kabeer', 'sagar']

# here we take input of a name
name1 = input("Name ? : ")
message_1 = welcome_students(name1) # we pass that name to function call
                                    # returned message is stored in message_1 variable

message_2 = welcome_students("Alex") # here we directly pass the name to function 
                                     # and stored the returned value in message_2 variable

print(message_1)                    # we print both messages
print(message_2)

# this is another way of using the function 
for name in students:
    print(welcome_students(name)) # we are using the function in for loop
                                  # and passing different names each time


