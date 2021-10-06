def OpenAndReadFirstStringOnFile():
	f=open('myfile.txt','r')

	firstline=f.readline()
	secondline=f.readline()
	print(firstline, end='')
	print(secondline, end='')

	f.close()