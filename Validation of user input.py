# Valudate user input exercise
#1. username is no more than 12 charactees
#2. username must not contain spaces
#3. usernamne must not contain digits

username = input("Enter username: ")
if len(username) > 12:
  print("Username can not be more that 12 characters")
elif not username.find(" ") == -1:
  print("username can't contain spaces")
elif not username.isalpha() :
  print("usename can't contain digits")
else:
  print(f"welcome {username}")