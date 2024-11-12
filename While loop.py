#while loop = execute some code wHILE some condition remain True

#name = input("Please Enter your name: ")

#while name == "":
#  print("You did not enter your name")
 # name = input("Please Enter your name: ")
#print(f"Hello {name}")
#here I have used while loop to continously prompt the user to type in their name, we can not continue until they type in something
#line 7= reprompt the user to type in an name (and it is within a while loop)
#line 8 exit the while loop first then print
#you do want someway to escape out of the while loop otherwise you will run into what is known as an infinite loop.. thats why we prompted the user to type in a name in line 7 (givjng them a chance to escape the infinite loop)

#age = int(input("Enter your age: "))

#while age < 0:
#  print("Age can't be negative")
#  age = int(input("Enter your age: "))

#print(f"You are {age} years old")

#num = int(input("Enter a Number between 1-10: "))

#while num < 1 or num > 10:
  #print(f"{num} is not valid")
#  num = int(input("Enter a Number between 1-10: "))

#print(f"Your number is {num}")

#my_list = [4,11,8,5,13,2]
#added_values = 1
#i = 0 

#while (added_values<20):
#  added_values += my_list[i]
#  i+= 1

## Break and continue

#Break
saved_password = 'password'
password_count = 0
while True:
  print(f"Your password count is {password_count}")
  if password_count<3:
    password_count+=1
    password = input("What is your password")
    if password == saved_password:
      break
    else :
      continue
  else:
    break