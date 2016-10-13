
def calculator(x,y,z):
    if y == "+":
        return int(x) + int(z)
    elif y == "-":
        return int(x) - int(z)
    elif y == "*":
        return int(x) * int(z)
    elif y == "/" or y == "\\" or y == ":":
        return int(x) / int(z)

start = "\033[1m"
end = "\033[0;0m"

while True:
    number_1 = input("Enter a number (or a letter to" + start + " exit" + end + "): ")
    try:
        number_1 == int(number_1)
    except ValueError:
        break
    operator = input("Enter an operation: ")
    number_2 = input("Enter another number: ")

    result = calculator(number_1, operator, number_2)

    print ("Result: " + str(result), end="")
    print ("\n")