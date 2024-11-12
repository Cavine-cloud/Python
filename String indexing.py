#Indexing = Allows us to access the elements of a sequence using []                       (indexing operator)
#          [start : end : step]

creditNumber = "1234-5678-9012-3456"

print(creditNumber[0])
print(creditNumber[:4])
print(creditNumber[5:9])
print(creditNumber[5:])
print(creditNumber[-1])
print(creditNumber[::2])

lastDigits = creditNumber[-4:]
print(f"XXX-XXX-XXX-{lastDigits}")

creditNumber = creditNumber[::-1]
print(creditNumber)

