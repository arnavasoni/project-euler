def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False # 0 and 1 are not prime
    p = 2
    while p * p <= n: # eg. p = 2; 4 < 120000
        if sieve[p]: # 2 is True
            for i in range(p * p, n+1, p): # 4, 6, 8, ...
                sieve[i] = False
        p += 1 # p = 3 now and so on
    primes = [i for i in range(n+1) if sieve[i]]
    return primes

primes = sieve_of_eratosthenes(120000)  # Generate prime numbers up to an arbitrary limit
print(primes[10000])  # The 10001st prime number
