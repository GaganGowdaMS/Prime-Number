def calculate(price,quantity=1):
    total=price*quantity
    return total
price=int(input("Enter the price:"))
print("The total amount is:",calculate(price))
