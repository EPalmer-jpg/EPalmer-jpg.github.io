import random
print("Rock, Paper, Scissors")
choices = ["rock", "paper", "scissors"]
player = "none"

while player !="quit":
	computer = random.randint(0,2)
	while player != "rock" and player != "scissors" and player != "paper":
		player = input("Enter rock, paper, or scissors: ")
	if player == choices[computer]:
		print("It's a tie!")
	if computer == 0:
		if player == "paper":
			print("You won!")
		if player == "scissors":
			print("You lost!")
	if computer == 1:
		if player == "scissors":
			print("You won!")
		if player == "rock":
			print("You lost!")
	if computer == 2:
		if player == "rock":
			print("You won!")
		if player == "paper":
			print("You lost!")
	player = input("type quit to end game or enter anything to continue ")