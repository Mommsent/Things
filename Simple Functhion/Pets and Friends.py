def pets():
	myPets=['Zophie', 'Pooka', 'Fat-tail']
	print('Enter a pet name:')
	name=input()
	if name not in myPets:
		print('I do not have a pet named ' + name)
	else:
		print(name + ' is my pet.')



birthdays={'Alice':'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
	print('Enter a name: (blank to quit)')
	name=input()
	if name=='':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birtday information for ' + name)
		print('What is their birthday?')
		bday=input()
		birthdays[name]=bday
		print('Birthday database updated.')


