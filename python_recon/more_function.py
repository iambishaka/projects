def bill():
    item = input("Item name : ")
    rate = float(input("Rate ? : "))
    qty = float(input("Quantity ? : "))

    total = rate*qty
    return {'Item' : item,   'Amount' : total}
    

bills = []

bills.append(bill())
bills.append(bill())
bills.append(bill())

for i in bills:
    print(i)

# items = [ 'sugar', 'paneer', 'cheese']
#
# for i in items:
#     print(i)
