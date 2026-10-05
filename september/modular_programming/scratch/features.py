def greet(name):
    return f"Hello, {name}!"



def discount(amount):
    if amount > 3000:
        discount = 0.3
        discounted_price = amount - (amount*0.3)
        return discounted_price
    if amount > 2000:
        discount = 0.2
        discounted_price = amount - (amount*0.2)
        return discounted_price
    if amount > 1000:
        discount = 0.1
        discounted_price = amount - (amount*0.1)
        return discounted_price
