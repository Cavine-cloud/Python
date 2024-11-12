#nested loop = a loop within a loop (outer, inner)
#           (a loop found within the code of another loop)
#             outer loop:
#                 inner loop:

for x in range(3):
  for y in range(1, 10):
    print(y, end="")
print()
#  blank print statent print a new line

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columbs: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(columns):
    print(symbol, end="")
print()