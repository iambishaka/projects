def create_username(name,year):
    username = name.lower()+str(year)
    return username
name = input("Enter your name.")
year = input("Enter your birth year.")

print("Your username: ", create_username(name,year))
