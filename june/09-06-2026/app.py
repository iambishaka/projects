print("Welcome to Bishaka Group of company ! ")
print("Please fill out the details below for the manajor position ")

name = input("Name: ")
age = int(input("Age: "))
city = input("city, town, village: ")
contact = int(input("Phone number: "))
gender = input("Gender: ")
experience = int(input("Experience in years: "))

with open("job_applications.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"City: {city}\n")
    file.write(f"Contact: {contact}\n")
    file.write(f"Gender: {gender}\n")
    file.write(f"Experience: {experience}\n")

