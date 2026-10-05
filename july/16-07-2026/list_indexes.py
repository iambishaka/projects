# ========== LIST INDEXES =============
# Every element on any list is automatically 
# assigned a inex number 
# index number starts with 0 
# first element is assigned index 0 , second one 1 and so on 
# for example 
items = ["Sugar", 2, 33.56]
# here in this list , there are 3 elements
# first item "Sugar" has index 0 
# 2 has index 1 
# 33.56 has index 2 
# suppose we want them to extract from list 
# and store in separate variables
# we can do this 
item_name = items[0]    # here we are accessing the first item using index number 0 
                        # then that value is assigned to variable 'item_name'
                        # now if you print 'item_name', What will be printed ? 
item_price = items[2]
item_qty = items[1]

# we create a new varaible here 
amount = item_price * item_qty

print(f"Item : {item_name}, QTY. {item_qty}, Rate : {item_price}") # using f-string syntax we can customize the output (print)
print(f"Total Amount {amount}")

