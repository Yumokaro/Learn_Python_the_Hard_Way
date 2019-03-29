from sys import argv
script, inputFile = argv

def printAll(f):
    print(f.read(), "\n")

def rewind(f):
    f.seek(0)

def printALine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

print("Print the whole file:\n")
printAll(currentFile)

print("now let's rewind.")
rewind(currentFile)

print("Print three lines:")
currentLine = 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)

currentLine += 1
printALine(currentLine, currentFile)