import numpy as np

eleven2twenty = np.arange(11, 21) # numbers 11 to 20

i = 2520 # already divisible by all numbers b/w 1 to 10

while i > 0:
    condition_true = np.mod(i, eleven2twenty) == 0 # i % all numbers between 11 to 20 is 0 for all?
    if np.all(condition_true):
        print(i)
        break
    i += 2520 # this makes sure that i is divisible numbers 1 to 10
