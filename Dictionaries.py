#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates
# examples Id: name , item:price

capitals = {"USA": "washington D.C","India": "New Delhi","China": "Beijing","Russia": "Moscow"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("USA"))

if capitals.get("Russsia"):
  print("The capital exists")
else:
  print("The capital doesn't exist")
  
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})
capitals.pop("China")
capitals.popitem()
capitals.clear

print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
   print(key)
  
values = capitals.values()
print(values)
 #To get all of the values within the dictionary
for values in capitals.values():
   print(values)