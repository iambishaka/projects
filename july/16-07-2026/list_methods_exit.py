 =========== LIST METHODS ===============
# append
# append method is used to add more items (or elements ) into the list 
# but it always adds the item a the end 
# suppose you have a list with 3 items 
list_1 = ["Sugar", 2.5, 33.45]
# and now you want to add something to this list 
# may the total amount 2.5 * 33.45 = 83.62 
# so you can do 
list_1.append(83.62)
# now after this list_1 has actually become 
# a list with 4 elements 
# list_1 = ["Sugar", 2.5, 33.45, 83.62]
# but you can only find it if you print the whole list 
# or all its elements 
# so let's print the whole list 
print(list_1)
# so you see all 4 elements are in it 
# let's start with an empty list  
friends = []
# let's print it 
print(friends)
# add one of your friend 
friends.append("Saron")
# now print the list again
print(friends)
# so you see , at first empy list is printed then 
# an element ( name of a friend is added)
# when we print it again , we see that elemnet 
# add some more friend names 
# and print the list every time you add a name 
friends.append("Ayeshna")
print(friends)
friends.append("Lochana")
print(friends)
