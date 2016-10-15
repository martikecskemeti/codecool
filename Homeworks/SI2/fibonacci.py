def fibonacci_numbers(n):
    fib = [0,1]
    for i in range(0,int(n) - 2):
        f_i = fib[i] + fib[i+1]
        fib.append(f_i)
    return fib

n = input("how many numbers?")

i = 0
for f in fibonacci_numbers(n):
    i += 1
    print (str(i) + "." + " " * (25 - len(str(i)) - len(str(f))) + str(f))
