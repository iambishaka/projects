
fla = True

while flag:
    n = int(input("Enter any number (0 to quit) : "))

    if n == 10:
        continue

    if n == 0:
        flag = False
        print("Bye Bye !")
        break

    print(f"You entered {n}, square of {n} = {n*n}")
