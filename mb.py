import random
while True:
	 x=input("enter 'r' to roll a dice and 'q' to quit")
	 if(x=='r'):
	 	print(random.randint(1,6))
	 elif(x=='q'):
	 	print("bye!")
	 	exit()
	 else:
	 	print("give either 'r' or 'q'")
