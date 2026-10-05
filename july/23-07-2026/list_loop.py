fruits = [
        "apple",
        "banana",
        "watermealon",
        "grapes",
        "pineapple",
        "guava"
        ]
l = len(fruits) # 6, l//2 = 6//2 = 3
# print(l)

# for i in range(l//2):
#     print("bishaka")

n = 10
# print(n//2)


stock = [
        'Milk', # 0 
         2.5,   # 1
         36.0,  # 2 
         'Bread',   # 0+3 = 3 
         3,         # 1+3 = 4 
         25.5,      # 2+3 = 5 
         'Egg', 
         8, 
         7.5, 
         'Cheese', 
         5, 
         22.5,
         'Pepper',
         2,
         33.5,
         'Salt',
         1,
         25.0
         ] # 15/3 = 5

stock_len = len(stock)

# print(stock_len//3)

idx = 0 
grand_total = 0

print(f"Item\t\tQty.\t\tRate\t\tAmount")
for i in range(stock_len//3):
    # print(stock[idx])           # at first loop idx = 0
    # print(stock[idx+1])
    # print(stock[idx+2])
    item = stock[idx]
    qty = stock[idx+1]
    rate = stock[idx+2]
    amount = qty * rate
    grand_total = grand_total + amount
    print(f"{item}\t\t{qty}\t\t{rate}\t\t{amount}")
    # print(f"{stock[idx]} {stock[idx+1]} {stock[idx+2]} {stock[idx+1]*stock[idx+2]}")

    idx = idx+3                 # idx = 3

print(f"\t\t\t\t Grand Total = {grand_total}")
