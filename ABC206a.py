
n = float(input())
tax_price = int(n*1.08)

if tax_price < 206:
    print("Yay!")
elif tax_price == 206:
    print("so-so")
else:
    print(":(")
