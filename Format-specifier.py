#format specifier = {value:flags} format a value based on what flags are                          inserted

price1 = 3000000.14159
price2 = -98700.65
price3 = 120000.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")
## 2 is the amount to be displayed and f is the floating point number

print(f"Price 1 is ${price1:20}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
#to allocate space to display a value, after the collon, add a number... ie 10

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")
#to precede a number with zero,after the collon,add a zero patted number...ie 010

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")
#to left justify a value, use a left angle bracket

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")
#to right justify a value, use a right angle bracket

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")