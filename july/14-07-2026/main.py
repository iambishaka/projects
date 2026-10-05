fruits = ["apple", "banana", "mango"]

# here 'fruits' variable is a 'list'
# when we store data in this format 
# inside [ ] brackets, separated by commas
# then python interpets it as 'list'
# There are certain features of lists
# like you can loop through list 
# ======== for loop ======= 

for f in fruits:
    print(f)

# here 'for' keyword is special word
# which will automatically create a loop 
# such feature is also called 'iterable'
# so after 'for' we can use any variable, 
# here we used 'f' , we could have use 'fruit' or
# 'item' or anything else, that will not make
# any difference, but that variable will give us 
# access to the items inside the list
# meaning, in each instance of loop 'f' will be 
# an item of the list 
# in the current case, we have 3 items inside list 
# those items are 'apple', 'banana' and 'mango'
# so for the first time 'f' is 'apple', second time 'banana'
# and so on
# 'for' loop will run only as many times as the number of
# in the list, for this case only 3 times 
# if there are more items, it will run that many times
# so we start with 'for' then a new variable like 'i' or 'f' or 'fruit'
# (to be clear, since we already named the list 'fruits' so new variable should not be same,
# 'fruits' is the list which is storing 3 fruits, 'fruit' is variable, which will hold 1 fruit at a time)
# then the name of the actual list => 'fruits'
# the list (fruits) should already be defined, or it will generate error
# then this line ends with : (colon)
# next line should start with usual python indentation (4 space preceeding line)
# any line which is indented after for loop statement is 
# inside the loop, meaning ?
# meaning - all those lines will be executed for the number of times
# loop runs 
# for example
numbers = [2, 5, 6, 7]
# in this list 'numbers' there are 4 items 
# so if we run a for loop for this list, the loop will run 4 times 
# we says same thing like this - 'loop will iterate 4 times'
for i in numbers:
    print(i)
# so here if we put more lines indented, those lines 
# will also be executed 4 times, like
for i in numbers:
    print(i)
    print("Hey Ya!")

# to be more clear
list_1 = [1,3,5,7] # 4 items
list_2 = ['neha', 'moon', 'jasmine'] # 3 itmes
# now if we run for loop
for l in list_1:
    print("hello world")

# here 'hello world' will be printed 4 times
# because there are 4 items inside the list (list_1)

# to make things clear , let's move to a new file
