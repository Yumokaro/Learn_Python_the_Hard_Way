theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'banana', 'coconut', 'grapes']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in theCount:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"element was: {i}")