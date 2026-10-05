import time
numbers_list = [1,18,90,91,46,83,44,38,36]

count = (0)

for i in numbers_list:
    print(f"checking, {i}")
    if i % 2 ==0 and i % 3 == 0:
        print(f"divisible by both 3 and 2")
    count = count + 1
    time.sleep(3)

print(f"Total count:{count}")
