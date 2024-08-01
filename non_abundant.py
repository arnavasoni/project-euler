import numpy as np
import math
total_sum = 0 # sum of all +ve integers that cannot be written as the sum of 2 abundant numbers
abundant_nums = []
population = np.arange(1, 28112) # 0 to 28123

for number in population[11:]: # the range is 12 onwards
    i = 1
    fac = [] # list of factors
    while i <= math.sqrt(number): # to find all factors
        if number%i == 0:
            fac.append(i)
            if number/i != i:
                fac.append(number//i)
        
        i += 1
    
    if number in fac: # remove number itself to get the proper divisors
        fac.remove(number)
    
    if sum(fac) > number:
        abundant_nums.append(number)

# print(abundant_nums)

sums = set()
n = len(abundant_nums)
for i in range(n):
    for j in range(i, n):
        sums.add(abundant_nums[i] + abundant_nums[j])

# sums = np.array(list(sums))
sums = list(sums)
remaining_population = np.setdiff1d(population, sums)
print(sum(remaining_population))