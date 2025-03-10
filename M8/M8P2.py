
fib1, fib2 = 0, 1 

print("First 20 Fibonacci Numbers:")

for i in range(n):
    print(fib1, end=" ")  
    next_fib = fib1 + fib2 
    fib1, fib2 = fib2, next_fib  