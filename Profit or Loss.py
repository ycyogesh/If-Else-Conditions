a = int(input("Enter Cost Price : "))
b = int(input("Enter Selling Price : "))


"""
   Profit   = Selling Price - Cost Price
   Loss     = Cost Price - Selling Price
"""

profit = b-a
loss = a-b

if(a>b):
    print("Loss",loss)
else:
    print("Profit",profit)
