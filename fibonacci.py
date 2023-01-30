def fibonacci(n):
    if n <= 0:
        print('enter the correct value')
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function with the first 10 terms of the Fibonacci sequence
p = int(input("enter your number:"))
for i in range(p):
    print(fibonacci(i))