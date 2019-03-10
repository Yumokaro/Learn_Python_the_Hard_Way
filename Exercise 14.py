from sys import argv

script, userName = argv
prompt = '\n>>> '

print(f"hi {userName}, i'm the {script} script.")
print("i'd like to ask you a few questions.")

print(f"do you like me {userName}?")
likes = input(prompt)

print(f"where do you live {userName}?")
lives = input(prompt)

print("what kind of comp do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer}. Nice.
""")
