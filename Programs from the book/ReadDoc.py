'''Skript for reading text file'''
with open('pi_didts.txt') as file_object: # open file as file_object
    contents = file_object.read()
    print(contents.rstrip()) # restrip - delete last empty string

