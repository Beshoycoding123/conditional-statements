cp=float(input("enter a cost price of a product: "))
sp=float(input("enter a selling price of a product: "))
if sp>cp:
    amount=sp-cp
    print("your profit is ",amount)
else:
    print("no profit")