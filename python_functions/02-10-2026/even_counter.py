import time

her_numbers = [ 33, 34, 35, 36, 37, 38]

count = 0

for i in her_numbers:
    print(f"Number = {i}, Remainder = {i%2}")
    if i%2 == 0:
        print("Even number, increase count by 1")
        count = count + 1
        time.sleep(3)
# loop ended

print(count)

