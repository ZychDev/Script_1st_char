import os 
import sys 
import fileinput

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'



FolderName = input("> ")
replacement = ""
print("How much first chars?")
space = input(">")
print("Replace with what?")
txtToReplace = input("> ")

for file in os.listdir(FolderName):
	if file.endswith(".txt"):

		print(bcolors.WARNING + "File name: " + bcolors.ENDC, os.path.join(FolderName,file))
		
		#open file 
		EditFile = open(file, 'r')
		lista = []
		while True:

			line = EditFile.readline()						
			if not line:
				break

			#print("linia: ", line)	
			new_line = "0" + line[space:]	
			#print("new line: ", new_line)
			change = line.replace(line, new_line)
			#print("trzeci: ", change)
			lista.append(change)
			#EditFile.close()
			#fout.write(change)
		#fout.close()
		
		fout = open(file, 'w')
		for i in lista:
			fout.write(i)
		fout.close()


	print("\n")


