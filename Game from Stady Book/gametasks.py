from os import remove,rename

def printInstructions(instruction):
	print(instruction)

def getUserScore(UserName):
	try:
		UserScore=open('userScores.txt', "r")

		for line in UserScore:
			content=line.split(', ')
			if content[0]==UserName:
				UserScore.close()
				return content[1]
			UserScore.close()
			return '-1'
	except IOError:
		print('File not found. A new file will be created.')
		UserScore=open('UserScores.txt', 'w')
		UserScore.close()
		return '-1'

def updateUserScore(newUser,userName,score):
	if newUser==True:
		file=open('userScore.txt', 'a')
		file.write(userName +',' + score + '\n')
		file.close()
	else:
		temp=open('userScore.tmp', 'w')
		file=open('userScore.txt', 'r')
	for line in file:
		content = line.split(', ')
		if content[0] == userName:
			temp.write(userName + ',' + score + '\n')
		else:
			temp.write(line)

	file.close()
	temp.close()
	remove('userScore.txt')
	rename('userScore.tmp', 'userScores.txt')


