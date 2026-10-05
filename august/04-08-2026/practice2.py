import time

n = [ 
     112,
     8,
     11,
     15,
     99,
     12,
     25,
     34,
     9,
     16
     ]


largest = n[0] # 8

for i in n:
    print(f"Largest number is {largest}")
    print(f"i = {i}")
    time.sleep(2)
    if i>largest:  
        print(f"hey {i} is greater than our largest , so i will replace it")
        time.sleep(3)
        largest = i

print(f"Largset number is {largest}")

