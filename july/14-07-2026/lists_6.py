# ========= LIST METHODS ========= 
items = ['sugar', 2, 72.14]

# you can find the length of a list
print(len(items))

# to be clear
# 'len' is a function which returns the length of any list
# you don't need to always print it 
# you can store it 
# compare it directly 
# for example 
# if you have list of names of your guests 
# and you want to check if there are more than 4 guests are or not 
guests = ['alex', 'john', 'electra', 'flash']
# now this list 'guest' have 4 elements in it 
# and you want to check if it has more than for items or not 
# you can do it like this 

number_of_guests = len(guests)  # see, here, numbers of the list will be stroed in 
                                # the variable 'number_of_guests'
                                # then we can use that value as we want 
# like 

if number_of_guests < 5:
    print("We need more people")

# let's put few more names manually
guests = ['alex', 'john', 'electra', 'flash', 'thor', 'daredevil'] # now it has 6 itmes in it 
number_of_guests = len(guests)          # we need to find the length once again
if number_of_guests > 5:                # so this line will evaluate to 'True'
    print("We have enough people")      # and as a result this line will be printed
