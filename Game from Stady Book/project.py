from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, MathGame, BinaryGame
try:
	mathInsructions="\nIn this game you need to decide simple exemple. " \
					"\nFor each correct answer you get 1 point. " \
					"\nFor wrong answer youl not losses the point."
	binaryInstructions="\nIn this game you get a decimal number. " \
					   "\nYour task is to convert this number in the binary number. " \
					   "\nFor each correct answer you get 1 point. " \
					   "\nFor wrong answer youl not losses the point."

	mg=MathGame()
	bg=BinaryGame()

	userName=input("\nPleas enter your username: ")
	score= int(getUserScore(userName))

	if score == -1:
		newUser = True
		score = 0
	else:
		newUser = False

	print('\nHello %s, welcome to the game.'%(userName))
	print('Your current score is %d.'%(score))

	userChoice = 0

	while userChoice != '-1':
		game = input('\nChuse "1" if you wont to play Math Game or "2" if Binary Game: ')

		while game != '1' and game != '2':
			print('You enter the incorrect number, pleas enter "1" or "2".')
			game = input('\nChuse "1" if you wont to play Math Game or "2" if Binary Game: ')
		numPrompt = input('\nHow many questions do you want per game (1 to 10)?: ')
		while True:
			try:
				num = int(numPrompt)
				break
			except:
				print('You did not enter the valid number. Pleas try again.')
				userResult = input('\nPleas, enter number of questions how do you want in the game (1 to 10): ')

except:
	pass

