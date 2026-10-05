# to be more clear
list_1 = [1,3,5,7] # 4 items
list_2 = ['neha', 'moon', 'jasmine'] # 3 itmes
# now if we run for loop
for l in list_1:
    print("hello world")

# here 'hello world' will be printed 4 times
# because there are 4 items inside the list (list_1)

# but if we just change the list name from list_1 to list_2 
# "hello world" will be printed 3 times, because there are 3 items in it 

for l in list_2:
    print("hello world")

# ============ TO BE NOTED ============ 
# notice one thing in above 2 for loops
# we are declaring 'l' variable after 'for' keyword
# but are not using it 

for l in list_2:            # l is declared , 
    print("hello world")    # but nowhere use
# so in such case , we can use a throaway variable

# like 
for _ in list_2:
    print("Hello Universe!")

# here we are taking reference of list_2 
# but items of that list are never used

# let's move to new file 
