from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, MathGame, BinaryGame
try:
	mathInsructions="\nВ этой игре вам предстоит решить простую арифметическую задачу. " \
					"\nЗа каждый правиьный ответ вам начислится одно очко. " \
					"\nЗа ошибочные ответы очки не вычитаются"
	binaryInstructions="\nВ этой игре вы получаете десятичное число. " \
					   "\nВаша задача - преобразовать кго в двоичную систему счисления. " \
					   "\nЗа каждый правильный ответ вам начислят одно очко. " \
					   "\nЗа ошибочные ответы очки не вычитаются."
	mg=MathGame()
	bg=BinaryGame()
	userName=input("\nPleas enter your username: ")
	score=int(getUserScore(userName))
	if score ==-1:
		newUser=True
		score=0
	else:
		newUser=False
	print('\nHello %s, welcome to the game.'%(userName))
	print('Your current score is %d.'%(score))

except:
	pass

