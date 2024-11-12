# if = Do some code only if some condition is true
# Else = Do something Else

age = int(input("Enter your age: "))

if age >= 18:
  print("You are signed up!!")
elif age < 0:
  print("You haven't been born yet")
else:
  print("You must be 18+ to sign up")