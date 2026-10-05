from helper import greet
from data import data
# modularization / modularisation 

print(greet("bISHAka", "Female", False))
print(greet("Savita", "Female", True))
print(greet("barun", "Male", True))


for entry in data:
    name = entry.get("user")
    gender = entry.get("gender")
    m = entry.get("Married")
    # print(m)
    print(greet(name, gender, m))






















def seq_length(dna):
    return len(dna)


dna = 'ATGCGATCGAT'
# print(f"Length : {seq_length(dna)}")


# def generate_invoice():
    # item = input("Item name : ")
    # rate = input("Rate : ")
    # try:
    #     rate = float(rate)
    # except:
    #     return "Invalid input, try again!"
    #
    # qty = input("QTY. : ")
    #
    # try:
    #     qty = int(qty)
    # except:
    #     return "Invalid input, try again!"
    #
    # return f"Item : {item} Total Amount : {(qty*rate):.2f} (for {qty} QTY.)"

# print(generate_invoice())


# item = input("Item name : ")
# rate = input("Rate : ")
# try:
#     rate = float(rate)
# except:
#     print("Invalid input, try again!")
#
# qty = input("QTY. : ")
#
# try:
#     qty = int(qty)
# except:
#     print("Invalid input, try again!")
#
# print(f"Item : {item} Total Amount : {(qty*rate):.2f} (for {qty} QTY.)")

