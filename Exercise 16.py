from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit 'ctrl-c'.")
print("if you do want that, hit 'return'.")

input("?")

print("opening file...")
target = open(filename, 'w')

print("truncating the file. bye!")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("i'm going to write these lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()