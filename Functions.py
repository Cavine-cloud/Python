# is a block of codes that executes a particular taskk on call
# #functions

# #pi*r*r*h

# def volume(height,radius):#function declaration
#     """function body"""
#     pi=3.142
#     calculatedVolume=pi*radius*radius*height
#     return calculatedVolume


# my_vol=volume(10,7) #function call
# print(my_vol)


# # Only use ordinary letters, numbers and underscores in your function names. They can’t have spaces, and need to start with a letter or underscore.
# # You can’t use Python's reserved words or keywords for function names, as discussed earlier with variable names. Here again is that table of Python's reserved words(opens in a new tab).
# # Try to use descriptive names that can help readers understand what the function does.


# """"print vs return in functions"""

# def _sayHello(message):
#     print("say hello")

# def ReturnHello(mesage):
#     return mesage


# my_message=_sayHello("hello world")#function call
# print(type(my_message))

# # variable scope
# #local variable & global variables


# #example of a global variable
# my_var="this is my global variable"

# def myFunction():
#     word="hello"    #example of a local variable
#     print(my_var)

# def MyFuction2():
#     print(my_var)
#     #print(word)

# MyFuction2()


# egg_count=0 #global variable

# def buy_eggs(count):
#     egg_count=count*12
#     print(f"your egg count is {egg_count} in the function block")
#     return None

# buy_eggs(1)

# print(f"your egg count is {egg_count}")


#function to check if a numer is odd or even
# def CheckNumber(number):
#     if number%2==0:
#         print("your number is an even number")
#     else:
#         print("your number is odd")

# CheckNumber(3)

def multiply(x,y):
    return x*y
resalt=multiply(2,4)
print(resalt)


#lambda functions
stillMultiply=lambda x,y:x*y
stillMultiply(2,4)

def volume(height,radius):  ## function declaration
  pi = 3.142
  calculated_volume = pi*radius*radius*height
  return calculated_volume
my_volume = volume(10,7)
print(my_volume)

# """"""ptint vs return in functions"""""
def _sayHELLO(message):
  print("say hello")
def ReturnHello(message):
  return message

my_message = _sayHELLO("hello world") ## function call
print(type(my_message))
##none is a data type 

        ## Variable scope
#Example of Global variables
my_variable = "This is me"
def my_function():
  word = "hello"
print(my_variable)
#print(word) ###error 

egg_count = 0
def buy_eggs(count):
  return count + 12
  
  # function to check if a number is odd or even
def check_number(number):
    if number % 2 == 0:
      print("Your number is an even number")
    else:
      print("Your number is an odd number")
      
check_number(5)

