from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"copying from {fromFile} to {toFile}")

inFile = open(fromFile)
inData = inFile.read()

print(f"the input file is {len(inData)} bytes long")

print(f"does the output file exist? {exists(toFile)}")
print("ready, hit RETURN to continue, ctrl-c to abort.")
input()

outFile = open(toFile, 'w')
outFile.write(inData)

print("done")

outFile.close()
inFile.close()
