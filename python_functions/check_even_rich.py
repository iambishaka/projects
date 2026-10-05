from rich.console import Console
console = Console()

def is_even(num):
    """Returns True if num is even, False otherwise."""
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    for i in numbers:
        if is_even(i):
            console.print(f"{i} is even number", style="green")
        else:
            console.print(f"{i} is odd number", style="red")

numbers = [11, 12, 13, 17, 19, 101, 3, 5, 15, 14, 77]


main()

