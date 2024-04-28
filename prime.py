def largestPF(num):
    PF = 1
    i = 2
    while i <= num/i:
        if num % i == 0:
            PF = i
            num //= i
        else:
            i += 1
    if PF < num: PF = int(num)
    
    return PF

a = 600851475143
print(largestPF(a))