n = [ 112, 8, 11, 15, 99, 12, 225, 25, 34, 9, 16 ]
# this will only print numbers above 50
for i in n:
    if i>50:
        print(i)

names = ['priya', 'annu', 'jasmine']
# this loop will not print name 'annu'
for name in names:
    if name == 'annu':
        continue

    print(name)


largest = n[-1] # we are holding last element 16 here 
# this loop will correctly find the largest number
for i in n:
    if i>largest:  
        largest = i

print(f"Largset number is {largest}")

