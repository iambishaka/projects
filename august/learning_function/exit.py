def check_even_and_odd(number):
    if number % 2 == 0:
        # print(number, "is even")
        return number, "is even"
    else:
        return number, "is odd"
        # print(number, "is odd")



print(check_even_and_odd(6))
print(check_even_and_odd(11))
print(check_even_and_odd(8))
print(check_even_and_odd(9))
print(check_even_and_odd(161))


def find_area(l,b):
    area = l*b
    return area


def calcualte_area():
    length = float(input("Enter length : ")) # 5.5
    breadth = float(input("Enter breadth : ")) # 10.0
    print(f"Area = {find_area(length,breadth)}")

calcualte_area()
calcualte_area()
calcualte_area()



    
