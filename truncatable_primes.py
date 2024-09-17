from prime_sample import *

def truncate(num):
    num_str = str(num) # converted the integer to string
    prime_count = 0
    # now we need a way to remove the digits from left to right
    for i in range(len(num_str)):
        if not prime(int(num_str[:i+1])) or not prime(int(num_str[i:])):
            return False
    return True

total = 0 # sum of the numbers in question
count = 0 # we need 11

i = 11
while count != 11:
    out = truncate(i)
    if out:
        total += i
        count += 1
        # print(i, total, count)
    
    i += 1

print(total)