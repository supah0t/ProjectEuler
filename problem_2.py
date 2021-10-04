#Finds sum of even valued terms in the Fibonacci sequence

def fibonacci(limit, fib1, fib2):
    evensum = 2
    fib1 = 1
    fib2 = 2
    fib3 = 0
    
    while True:
        fib3 = fib1 + fib2
        if fib3 > limit:
            return evensum
        fib1 = fib2
        fib2 = fib3
        if fib3%2 == 0:
            evensum += fib3
            
x = int(input("Number bellow which to find sum of even-valued terms in the Fibonacci sequence: "))
            
print(fibonacci(x, 1, 2))