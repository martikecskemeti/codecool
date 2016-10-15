import sys
import operator

my_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "\\": operator.truediv,
    ":": operator.truediv  
}

def calculator(x,y,z):
    try:
        return y(int(x),int(z))
    except ZeroDivisionError:
        return "Division by zero."
        
def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    
def bold(text):
    return "\033[1m" + text + "\033[0;0m"
    
    
while True:
    n1 = input("Enter a number (or a letter to " + bold("exit") + "): ")
    if not is_int(n1):
        break
                                      
    while True:
        op = input("Enter an operation: ")
        if op in my_operators.keys():
            break
        print("Try again, not a valid operator: " + ", ".join(o for o in my_operators.keys()))
    
    while True:
        n2 = input("Enter another number: ")
        if is_int(n2):
            break
        print("Try again, not a valid integer.")
    
    result = calculator(n1, my_operators[op], n2)

    print ("Result: " + str(result), end="")
    print ("\n")

print("Bye!")
