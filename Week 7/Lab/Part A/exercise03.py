def is_prime(n):
    if n <2:
        return False
    else:
        for i in range(2, int(n**0.5) +1):
            if n % i == 0:
                return False
        return True

def display_primes(limit):
    for i in limit:
        if is_prime(i):
            print(i)

print(display_primes([1,2,3,4,7,10,17,25]))