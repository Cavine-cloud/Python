#collection = single "variable" uswd to store multiple values
#      list = [] ordered and changaeble. Duplicates OK
#       set = {} unordered and immutable, but add/remove OK. NO Duplicates
#     tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "babana", "coconut"]
print(fruits)
#to access one of these elements on rhe list, you can use the index operator ie. print(fruits[0])- for the first element,, print(fruits[3])- for the fourth element,
#you can access the first three, ie. print(fruits[:3]), you can even use a step, like I would like every second element beginning from index zero that is apple ie. print(fruits[::2]), maybe i'd like the fruits backward, I'll set my step to index -1 ie. print(fruits[::-1])
#you can use the index operator with collections much like you can use with strings.

   ##you can also iterate over collections with the for loop

for fruit in fruits:
  print(fruit)
  
   ##to list the different methods we can use with collections
print(dir(fruits))
print(help(fruits))

#if you need the length of how many elements are within a collection
print(len(fruits))

#to find is a value is within a collections
print("orange" in fruits)

#lists are changeable ie
fruits[0] = "pineapple"
for fruit in fruits:
  print(fruit)

#to add a value, use append, to remlve use remove, insert , sort

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapples")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("orange"))
print(fruits.count("banana"))
print(fruits)

         ##set
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)