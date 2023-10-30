def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation.")
print("+")
print("-")
print("*")
print("/")

while True:
    choice = input("Enter choice(+/-/*//): ")
    if choice in ('+', '-', '*', '/'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '+':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '-':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '*':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '/':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
          break
    else:
        print("Invalid Input")
