def is_even(num):
    """Returns True if num is even, False otherwise."""
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    for i in numbers:
        if is_even(i):
            print(f"{i} is even number")
        else:
            print(f"{i} is odd number")

numbers = [11, 12, 13, 17, 19, 101, 3, 5, 15, 14, 77]


main()

