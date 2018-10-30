#import the random package so that we can generate random numbers
from random import randint

#choices is an array=> a container that can hold multiple items
#arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

#make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

#print the choice to the terminal window
print("Computer chooses: ", computer_choice)

computer_lives = 3

player_lives = 3

#set players to false
player = False

while player == False:
#set player to True
	player = input("Rock, Paper, Scissors?")
	if player == computer_choice:
		print("Tie!")
	elif player == "Rock":
		if computer_choice == "Paper":
			print("You lose!", computer_choice, "covers", player)
			player_lives = player_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
		else:
			print("You win!", player, "smashes", computer_choice)
			computer_lives = computer_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
	elif player == "Paper":
		if computer_choice == "Scissors":
			print("You lose!", computer_choice, "cut", player)
			player_lives = player_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
		else:
			print("You win!", player, "covers", computer_choice)
			computer_lives = computer_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
	elif player == "Scissors":
		if computer_choice == "Rock":
			print("You lose!", computer_choice, "smashes", player)
			player_lives = player_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
		else:
			print("You win!", player, "cuts", computer_choice)
			computer_lives = computer_lives - 1
			print("Player has", player_lives, "lives left")
			print("Computer has", computer_lives, "lives left")
	else:
		print("Not a valid move! Try that again.")

	player = False

	if computer_lives == 0 or player_lives == 0:
		print("Game over. Good game! Would you like to play another match?")
	
	play_again = input
		
	if play_again == "Yes":
		player == False
	
	elif play_again == "No":
		player == True  

	computer_choice = choices[randint(0,2)]