def cheeseAndCrackers(cheeseCount, boxes):
    print(f"you have {cheeseCount} cheeses.")
    print(f"you have {boxes} boxes of crackers.")
    print("that is enough for a party!!")
    print("make me a hat.\n")

print("we can give the function directly ::")
cheeseAndCrackers(20, 30)

print("or, we can use vars from our script ::")
cheeseAmount = 10
crackersAmount = 50

cheeseAndCrackers(cheeseAmount, crackersAmount)

print("we can also do math with it ::")
cheeseAndCrackers(10+20, 5+6)

print("We can also combine vars and math ::")
cheeseAndCrackers(cheeseAmount + 100, crackersAmount + 1000)
