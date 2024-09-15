import math

def digit_fact_sum(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum += math.factorial(digit)
        num = num // 10
        # print(digit, num)
    
    return sum

total = 0

for i in range(3, 7*math.factorial(9)):
    number_sum = digit_fact_sum(i)
    if number_sum == i:
        total += i

print(total)