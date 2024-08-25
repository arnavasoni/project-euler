from itertools import permutations

a = '0123456789'
perms = list(permutations(a, 10))
print(''.join(perms[1000000-1]))
