
################# WHILE LOOPS ARE INFINITE, IF NOTHING CHANGES THEM TO FALSE OR FALSEY THEY RUN FOREVER #################

msg = input("What's the secret password? ")
while msg != "bananas":
	print("Wrong!")
	msg = input("What's the secret password? ")
print("Correct!")


#######convert for loop into while loop#############

for num in range(1,11)
	print(num)

num = 1
while num < 11:
	print(num)
	num += 1

############## WHILE LOOP EMOJI EXERCISE ################

for num in range(1,11):
	print("&" * num)

num = 1
while num < 11:
	print("&" * num)
	num += 1

########## EMOJI PYRAMID #############

num = 1
x = 18
y = 18
while num < 20:
	space = " "
	print((space * x) + ("&" * num) + (space * y))
	num += 2
	x -= 1
	y -+ 1


num = 1
while num < 20:
	str = "&" * num
	print(str.center(40))
	num += 2

########### COLT TALKING TO HIS SISTERS EXERCISE #################

msg = input("Hey, how's it going? ")
while msg != "stop copying me":
	msg = input(msg + " ")
print("ugh, fine.")


**
msg = input("Hey, how's it going? ")
while msg != "stop copying me":
	print(msg)
	msg = input()
print("ugh, fine.")
**


msg = input("Hey, how's it going? ")
while msg != "stop copying me":
	msg = input(f"{msg}\n")
print("ugh, fine.")


########### Random Number Guessing Game ################

from random import randint  

random_number = randint(1,10) 

guess = input("Guess a number between 1 and 10: ")

guess = int(guess)

cont = "y"

while cont != "n":
	guess = int(guess)
    if guess == random_number:
    	print("You guessed it! You won!")
    	cont = input("Do you want to keep playing? (y/n)")
    	if cont != "y" or cont != "n":
    		input("Do you want to keep playing? (y/n)")
    elif guess < random_number:
    	print("Too low, try again!")
    	guess = input("Guess a number between 1 and 10: ")
    else: 
    	print("Too high, try again!")
    	guess = input("Guess a number between 1 and 10: ")

while guess != random_number:
	guess = int(guess)
	if guess < random_number:
    	print("Too low, try again!")
    	guess = input("Guess a number between 1 and 10: ")
    else: 
    	print("Too high, try again!")
    	guess = input("Guess a number between 1 and 10: ")
print("You guessed it! You won!")
    cont = input("Do you want to keep playing? (y/n)")
    if cont != "y" or cont != "n":
    	input("Do you want to keep playing? (y/n)")


### simplest solution ###
from random import randint  

random_number = randint(1,10) 
guess = None

while guess != random_number:
	guess = input("Guess a number between 1 and 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else:
		print("You won!!")

##### More advanced #####
from random import randint  

random_number = randint(1,10) 

while True:
	guess = input("Guess a number between 1 and 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too low, try again!")
	elif guess > random_number:
		print("Too high, try again!")
	else: 
		print("You guessed it! You won!")
		cont = input("Do you want to keep playing? (y/n) ")
		if cont == "y":
			random_number = randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break