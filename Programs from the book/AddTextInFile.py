from ReadFileAcrossCycle import ReadFileAcrossCycle
def AddTextInFile():
	f=open('myfile.txt','a')
	f.write('\nThis sentence will be append.')
	f.write('\nPython is Fun!')
	f.close()
	ReadFileAcrossCycle()
AddTextInFile()
