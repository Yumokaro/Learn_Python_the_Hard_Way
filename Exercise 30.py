people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")

else:
    print("we can't decide. they're equal.")


if trucks > cars:
    print("too many trucks.")
elif trucks < cars:
    print("take all the trucks.")
else:
    print("still can't decide.  theyre equal")


if people > trucks:
    print("take only trucks.")
else:
    print("stay home.")
