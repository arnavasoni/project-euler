import math

prod = int(math.pow(2, 1000))
sum = 0

while prod > 0:
    digit = prod % 10
    sum += digit
    prod = prod//10

print(sum)