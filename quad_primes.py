import cmath # for complex maths

# function to check if prime number
def isprime(n):
    if n == 1:
        return False
    
    # if n == 2:
    #     return True
    i = 1
    count = 0
    factors = []
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            count += 1
            if n/i != i:
                factors.append(int(n/i))
                count += 1

        i += 1
    
    if count == 2:
        return True
    else:
        return False

print(isprime(2))
