items = ['Sugar', 1.5, 44.25]

item_1 = items[0] # sugar
item_2 = items[2]   # 44.25
item_3 = items[1]   # 1.5

# total_amount = round((item_2 * item_3), 1) # round(22.5, 0) 
total_amount = item_2 * item_3

print(f"total amount = {total_amount:.2f}")
