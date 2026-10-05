stock = ['Milk', 2.5, 36.0, 'Bread', 3, 25.5, 'Egg', 8, 7.5]

item_1 = stock[0] 
q_1 = stock[1]
r_1 = stock[2]
a_1 = q_1 * r_1 

item_2 = stock[3]
q_2 = stock[4]
r_2 = stock[5]
a_2 = q_2 * r_2

item_3 = stock[6]
q_3 = stock[7]
r_3 = stock[8]
a_3 = q_3 * r_3

g_t = a_1+a_2+a_3

print(f"Item\t\tQty.\t\tRate\t\tAmount")
print(f"{item_1}\t\t{q_1}\t\t{r_1}\t\t{a_1}")
print(f"{item_2}\t\t{q_2}\t\t{r_2}\t\t{a_2}")
print(f"{item_3}\t\t{q_3}\t\t{r_3}\t\t{a_3}")
print(f"\t\t\t\tTotal Amount = {g_t}")



# Item    Qty.    Rate    Amount
# Milk    2.5     36.0    90.0
# Bread   3       25.5    76.5 
# Egg     8       7.5     60.0
#
# Total Amount            226.5
