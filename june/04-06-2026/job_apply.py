print("Welcome to Bishaka Groups of Company!")
print("Please fill out the details below for the Receptionist position.")

name = input("Name : ")
age = int(input("Age : "))
city = input("City/Town/Village : ")
contact = int(input("Phone number : "))
gender = input("Gender ? (M/F/O) : ")
experience = int(input("Experience in years : "))

with open("job_applications.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"City: {city}\n")
    file.write(f"Contact: {contact}\n")
    file.write(f"Gender: {gender}\n")
    file.write(f"Experience: {experience}\n")
    file.write("-----------------\n")

print("-------- Results ---------- ")
if experience >= 2:
    print(f"Congratulations {name}! You have been selected for the next round.")
    print("Hope to see you in team soon, good luck!")
else:
    print(f"Thank you {name} for your time!")
    print("Sorry, you do not meet the minimum requirement of 2 years!")
