import time

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
    if n <2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

start = time.perf_counter()
print(fibonacci_recursive(40))
end = time.perf_counter()

print("Execution time:", end - start, "seconds")

# input 10
## iterative - 2.1856000330444658e-05 seconds
## recusive - 2.9662000088137574e-05 seconds

# input 20
## iterative - 2.3313999918173067e-05 seconds
## recursive - 0.0007148179997784609 seconds

# input 30
## iterative - 2.5276000087615103e-05 seconds
## recursive - 0.13704314299957332 seconds

# input 35
## iterative - 3.212999990864773e-05 seconds
## recursive - 1.2512222989998918 seconds

# input 40
## iterative - 2.9369000003498513e-05 seconds
## recursive - 13.893050547999792 seconds

# note: the execution times were not consistent at all - re-running it multiple times would give a different value
# recursive seemed to get much slower past input 30