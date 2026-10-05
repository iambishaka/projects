# src/my_package/__main__.py 

from my_package.core.engine import greet,gst
from my_package.utils.helpers import compare

def main():
    a = input("Enter first number :")
    b = input("Enter second number :")
    result = compare(a,b)
    print(f"Number comparison result : {result} is bigger")
    print(greet("Alice"))
    tax = gst(2000, 12)
    print(f"GST Amount: {tax}")

if __name__ == "__main__":
    main()
