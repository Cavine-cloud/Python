#for loops = execute a block of code a fixed number of NotImplemented
#            you can iterate over a range, string , sequence etc

for counter in range(1, 11):
  print(counter)

for counter in reversed(range(1, 11)):
  print(counter)
print("HAPPY NEW YEAR!!!!")

for counter in reversed(range(1, 11, 2)):
  print(counter)
print("HAPPY NEW YEAR!!!!")
#step... if you would like to count by 2 or 3 or 4 etc... second comma then the step you want to take

for x in range(1, 21):
  if x == 13:
    break
  else:
    print(x)
  