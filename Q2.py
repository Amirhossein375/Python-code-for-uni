amount = float(input("Inter amount of rice (Kg):"))
price = float(input(" Inter price of rice :"))
min = amount* price - amount*price*0.15
max = amount* price + amount*price*0.15
print(f" min of price is {min} and max of price is {max}")
