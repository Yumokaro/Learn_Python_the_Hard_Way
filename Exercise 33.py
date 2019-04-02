i = 0
numbers = []

while i < 6:
    print(f"adding a value to the array.  Element #{i} has been added.")
    numbers.append(i)

    i = i+1

print("The Array has this range of values:")
for num in numbers:
    print(num)