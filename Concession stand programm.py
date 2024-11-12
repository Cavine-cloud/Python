#we will use dictionary to keep track of a menu item and an associated price

menu = {"pizza": 1000.50,"nachos": 900.00,"popcorn": 100.25, "fries": 250.75,"chips": 90.00,"soda": 70.50,"lemonade": 160.25}
cart = []
total = 0
#to keep track of the user selected items I will create an empty list named cart
#I will also declare avariable named total ,to keep track of the total 

print("-------MENU-------")
for key, value in menu.items():
  print(f"{key:10}: Ksh.{value:.2f}")
print("--------------------------")

#we will ask a user for some input like what Item would they like to buy from the menu
while True:
  food = input("select an item(q to quit):" ).lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

print("------------YOUR ORDER--------------")
for food in cart:
  total += menu.get(food)
  print(food, end=" ")

print()
print(f"Total is: Ksh.{total:.2f}")