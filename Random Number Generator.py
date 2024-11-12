import random
#print(help(random))

low = 1
high = 100
options = ( "rock", "papper", "scissors")
number = random.randint(1, 6)

##if you need a random floating point number
number = random.random()
print(number)

option = random.choice(options)
print(option)