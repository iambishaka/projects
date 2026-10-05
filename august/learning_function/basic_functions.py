menu_items = [
        "Espresso", True, 120,  
        "Cappucino", True, 110,
        "Cold Brew", True, 150,  
        "Masala Chai", False, 50,
        "Lassi", True, 70
        ]

def welcome():
    print("======================================")
    print("   Welcome to Barun's Coffee Corner   ")
    print("======================================")

def greet(name):
    print(f"Hey , {name}, What would you like to have today ?")

def show_menu():
    # for item in menu_items:
    idx = 0
    for _ in range(len(menu_items)//3):
        item = menu_items[idx]
        available = menu_items[idx+1]
        price = menu_items[idx+2]
        if available == True:
            print(f"Item : {item}, Price : {price}")
            print_divider(30)

        idx = idx + 3

def print_divider(n):
    print("-"*n)


welcome()
greet("Biren")
show_menu()






