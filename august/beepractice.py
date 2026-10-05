user = ["rajesh",19,"neha",17,"rohan",20,"sushma",15,"sanjita",16,"bepasha",10,"aarav",5,"bishu",14] # Database

user_len = len(user)                        # length of the database

name = input("Enter Your Name ")            # the name user is looking for

idx = 0                                     # index count 

for i in range(user_len//2):                # for loop startrs for the pair of 2 
    user_name = user[idx]                   # this is the user name from database
    age = user[idx+1]

    if name == user_name:                   # we are checking if name from database and name user looking is same or not 
        if age < 15 :                       # if name is found then only we will check the age
            print(name,"is under age - Not eligible")
        else :
            print(name,"is allowed")


    idx = idx+2

    


# Functions



 
