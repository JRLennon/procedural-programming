def factorial_iterative(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

def factorial_recursive(n):
    if n < 2:
        return n
    else:
        return n * factorial_recursive(n-1)

print(factorial_iterative(5)) 
print(factorial_recursive(5))