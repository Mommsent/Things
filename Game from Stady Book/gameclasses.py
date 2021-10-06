class Game:

	def __init__(self,no0fQuestions=0):
		self._no0fQuestions=no0fQuestions

	@property
	def no0fQuestions(self):
		return self._no0fQuestions

	@no0fQuestions.setter
	def no0fQuestions(self,value):

		if value < 1:
			self._no0fQuestions = 1
			print('\nMinimum Number of Questions = 1')
			print('Hence, number of questions will be set to 1')
		elif value > 10:
			self._no0fQuestions = 10
			print('\nMaximum Number of Questions = 10')
			print('Hence, number of questions will be set to 10')
		else:
			self._no0fQuestions= value

class BinaryGame(Game):
	def generateQuestions(self):
		from random import randint
		score=0

		for i in range(self.no0fQuestions):
			base10=randint(1,100)
			userResult=input('\nPlease convert %d to binary: ' %(base10))

			while True:

				try:
					answer=int(userResult, base = 2)
					if answer==base10:
						print('You entered the correct answer')
						score+=1
						break
					else:
						print("Wrong answer. The correct answer is {:b}.".format(base10))
						break
				except:
					print('You did not enter a binary number. Pleas try again.')
					userResult=input('\nPleas convert %d to binary: ' %(base10))

			return score

class MathGame(Game):
	def generateQuestions(self):
		from random import randint
		score=0
		numberList=[0,0,0,0,0]
		symbolList=[' ',' ',' ',' ']
		operatorDict={1:' + ', 2:' - ', 3:' * ', 4:' ** ' }

		for index in range(self.no0fQuestions):
			for index in numberList:
				numberList[index] = randint(1,9)

			for index in range(0,4):
				if index > 0 and symbolList[index -1]=='**':
					symbolList[index]=operatorDict[randint(1,3)]
				else:
					symbolList[index]= operatorDict[randint(1,4)]

		questionString=str(numberList[0])

		for index in range(0,4):
			questionString+ str(numberList[index+1])+symbolList[index]

		result=eval(questionString)
		questionString=questionString.replace('**', '^')
		userResult=input("PLeas, enter your answer: ")

		while True:

			try:
				answer = int(userResult)
				if answer == result:
					print('You entered the correct answer!')
					score += 1
					break
				else:
					print("Wrong answer. The correct answer is {:b}.".format(result))
					break
			except:
				print('You did not enter the valid number. Pleas try again.')
				userResult = input('\nPleas, evaluate %s: '%(questionString) )

		return score