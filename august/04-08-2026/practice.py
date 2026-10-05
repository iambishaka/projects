n = [ 
     15,
     12,
     25,
     34,
     9,
     16
     ]

total = 0 

# loop starts here
for i in n:
    total= total+i  # anything in indentation is inside loop
# loop ends 

# print(f"total = {total}")

items = [ 'sugar', 35.78, 1.5, 'butter', 10.0, 5, 'bread', 25.0, 2]

total = 0
idx = 0
for i in range(len(items)//3):
    item_name = items[idx]
    item_rate = items[idx+1]
    item_qty = items[idx+2]

    amount = item_rate*item_qty
    total = total + amount

    print(f"{item_name} @Rs.{item_rate} QTY {item_qty} {item_rate*item_qty}")

    idx = idx + 3 

print(f"Tota Amount : {total:.2f}")
