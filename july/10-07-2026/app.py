amount = float(input("Enter the item price : "))
# gst = amount * 0.18
gst = amount * 0.12
total_amt = amount + gst 
print(f"Total Amount with GST = {total_amt}")
