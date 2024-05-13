import numpy as np

'''
conditions: a2 + b2 = c2
a < b < c
a + b + c = 1000
abc = ?
'''

for a in range(1, 1000):
    for b in range(a, 1000 - (2*a)): # b > a, so the max value b can have is 1000 - 2*a 
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)