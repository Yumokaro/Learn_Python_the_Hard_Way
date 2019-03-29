def add(a, b):
    print(f"this is adding {a} + {b}.")
    return a + b

def sub(a, b):
    print(f"this is subtracting {a} - {b}.")
    return a - b

def mult(a, b):
    print(f"this is multiplying {a} x {b}.")
    return a * b

def div(a, b):
    print(f"this is dividing {a} / {b}.")
    return a / b

print("Time for maths!\n")

age = add(30, 5)
height = sub(78, 4)
weight = mult(90, 2)
iq = div(100, 2)

print(f"\nAge: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")
