import random

print("WELCOME TO THE GAME,THE ROCK PAPER SCISSORS")

iswin = False
playerinput=0
while iswin == False:
	print("")
	print("press 1 for Rock.")
	print("press 2 for Paper.")
	print("press 3 for Scissors.")
	while(playerinput==0):
		playerinput = int(input("what would you like to play?"))

	computerinput= random.randint(1,3)

	if (playerinput == 1) and (computerinput == 1):
		iswin = False
		print("it's a draw; you both played Rock!")	
	if (playerinput == 2) and (computerinput == 1):
		iswin = True
		print("you win; computer played Rock!")
	if (playerinput == 1) and (computerinput == 2):
		iswin = True
		print("you lose; computer played paper!")
	if (playerinput == 3) and (computerinput == 3):
		iswin = False
		print("it's a draw; you both played Scissors!")
	if (playerinput == 2) and (computerinput == 2):
		iswin = False
		print("it's a draw; you both played Paper!")
	if (playerinput == 3) and (computerinput == 1):
		iswin = True
		print("you win; computer played Rock!")
	if (playerinput == 1) and (computerinput == 3):
		iswin = True
		print("you lose; computer played Scissors")
	if (playerinput == 3) and (computerinput ==2):
		iswin = True
		print("you win; computer played paper!")
	if (playerinput == 2) and (computerinput == 1):
		iswin = True
		print("you win; computer played Rock!")				


















