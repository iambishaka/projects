user = ["rajesh",19,"neha",17,"rohan",20,"sushma",15,"sanjita",16,"bepasha",10,"aarav",5,"bishu",14] # Database
# agents = ["raj", "aakash", "krishna", "harry", "sneha", "sonia", "jasmine"]

def entry(name, age):
    if age <= 15:
        return f"Hello, {name}, you are not eligible"

    if age > 15:
        return f"Hello, {name}, you are welcome !"


def search_name(name, data):
    n = 0
    l = len(data)//2
    for i in range(l):
        if data[n]==name:
            return entry(data[n], data[n+1])

        n = n+2

    return f'Name {name} not found'


name = input("Enter name : ")

print(search_name(name, user))
