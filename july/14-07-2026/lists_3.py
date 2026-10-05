items = [11, 15, 17]

# suppose you want to double each number of the list
# you can do it like this 
for i in items:     # every time i will be a number from that list (items)
    print(i*2)      # to double , we multiply with 2 (i * 2)

# but you don't want to use the items inside the loop
# you just want to iterate (run the loop) for that many times 
# you can do it like this 
for _ in items:             # throw away variable _
    print("Hello Universe!!!")

# you can argue , what is wrong if just 'i' or 'l'
# nothing, it will work fine , but , but 
# in computer, memory is very costly
# when you write 'l' or 'i' or any random variable
# it will consume some memory from your host computer 
# for bigger real life application it will make huge difference 
# it can slow down the application

# ======== NEXT ====>
