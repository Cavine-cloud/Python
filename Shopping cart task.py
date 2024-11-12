foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy (q to quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of a {food}: Ksh."))
    foods.append(food)
    prices.append(price)

print("-----YOUR CART-----")
#decorative text, display shopping card

for food in foods:
  print(food)
#I will the iterate over all the elements found within my foods list
#if yiy want to horizontally list tge foods, print(food, end=" ")

for price in prices:
  total += price
print()
print(f"Your TOTAL is: {total} Ksh.")
#we'll need to iterate and add up all prices