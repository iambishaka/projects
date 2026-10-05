
mobiles = [
    "Samsung",
    18000,
    12,
    2,
    4.5,
    "Realme",
    14000,
    18,
    1,
    4.3,
    "Vivo",
    21000,
    10,
    2,
    4.4,
    "OnePlus",
    32000,
    6,
    2,
    4.8,
    "Motorola",
    17000,
    15,
    1,
    4.2
]

i = 0

# length = len(mobiles)

print(f"Brand\t\tPrice\t\tStock\t\tWarranty\tRating")
for m in range(len(mobiles)//5):
   b = mobiles[i]
   p = mobiles[i+1]
   s = mobiles[i+2]
   w = mobiles[i+3]
   r = mobiles[i+4]
   print(f"{b}\t\t{p}\t\t{s}\t\t{w}\t\t{r}")

   i = i + 5


# Brand       Price       Stock       Warranty        Rating
# Samsung     18000       12          2               4.5          
