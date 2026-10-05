print("Welcome to our Company! ")

print("please fill out the details below to apply for the Receptionist position.")

name = input("Enter your name : ")
age = input("Enter your age : ")
details = input("Enter your personal details (e.g, city, contact): ")
experience = int(input("Enter yoour years of experience : "))

print("------results---------")

if experience >= 2:

    print(f"Congratulations {name}! You have been selected for the next round. ")
    print("Welcome to the team ! ")
else:   
    print(f"Thank you for your time ,{name}.")
    print("sorry,you do not meet the minimum requirement of 2 years of experience.")


