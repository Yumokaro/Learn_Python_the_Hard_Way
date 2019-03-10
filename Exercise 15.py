from sys import argv

script, filename = argv

## filename = Ex15text
txt = open(filename)

print(f"here's your file - \n\n{filename}:")
print(txt.read(), "\n")

print("type the filename again:")
fileAgain = input(">>> ")

txtAgain = open(fileAgain)

print(txtAgain.read())
