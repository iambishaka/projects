def even_counter(data):
    if not data:        # if there are not data , we return None
        return None

    counter = 0 # we initialize the counter with 0

    for i in data:
        """ We need to skip counting 0 """
        if i == 0:
            continue
        """ if remainder is 0 when divided by 2, we increment the counter by 1"""
        if i%2 == 0:
            counter = counter + 1

    """ Finally we return the counter to caller """
    return counter

print(even_counter([1, 2, 3, 4, 5, 6])) # for this call function returns on line no. 11
print(even_counter([])) # for this call function returns on line no. 3

my_numbers = [3,5,7,8,9,10, 0, 0]
result = even_counter([4,65, 78, 83]) # here python is the caller, to store the value in variale
print(result)

print(even_counter(my_numbers))









# print(bool(10>19))

# print(bool([]))
