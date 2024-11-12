#conditional expressions = A one line shortcut for the if-else statements                               (ternary operator)
  #                          x if condition else y
  
number = 2
a = 6
b = 7
age = 13
tempereature = 30
userRole = "admin"

#print("positive" if number > 0 else "negative"),
#result = "EVEN" if number % 2 == 0 else "ODD"
#maxNum = a if a > b else b
#minNum = a if a < b else b
#status = "adult" if age >= 18 else "child"
#weather = "Hot" if tempereature >25 else "Cold"
accessLevel = "Full access" if userRole == "admin" else "Limited access"
print(accessLevel)