# you would like to count the number of your fruits in your basket.
# in order to do this, you have the following dictionary and list of fruits.
# use the dictionary and list to count the total number of fruits, but you do not want to count the other items ij your basket.

result = 0
basket_items = {"apples" : 4 , "oranges" : 19, "kites" : 3, "sandwiches" : 8}
fruits = ["apples", "oranges", "pears", "grapes", "banana"]

# iterate through the dictionary

for item in basket_items:
  if item in fruits:
    no_fruits = basket_items[item]
    result += no_fruits
# if the key is in the list of fruits, add the value (number of fruits) to result

