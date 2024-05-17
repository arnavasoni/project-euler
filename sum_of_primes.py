def isprime(num):
    if num == 1:
        return 0 # not prime, not composite
    
    if num == 2:
        return 2 # 2 is prime
    
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return 0 # if composite, return 0 cuz you don't wanna add composite numbers
        
        return num # if prime, the number should be added to the sum

sum = 0
for number in range (2000000, 2, -1):
    sum += isprime(number)

print(sum)