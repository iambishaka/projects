stock = ['Milk',2.5,36.0,'Bread',3,25.5,'Egg',8,7.5,'Cheese',5,22.5,'Pepper',2,33.5,'Salt',1,25.0] 

stock_len = len(stock)
idx = 0 
grand_total = 0
print(f"Item\t\tQty.\t\tRate\t\tAmount")
for i in range(stock_len//3):
    item = stock[idx]
    qty = stock[idx+1]
    rate = stock[idx+2]
    amount = qty * rate
    grand_total = grand_total + amount
    print(f"{item}\t\t{qty}\t\t{rate}\t\t{amount}")
    idx = idx+3

print(f"\t\t\t\t Grand Total = {grand_total}")
