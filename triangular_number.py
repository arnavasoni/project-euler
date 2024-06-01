# credits to the solution (with explanation: https://stackoverflow.com/questions/17743851/optimise-the-solution-to-project-euler-12-python)

import math

def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i) # to get the factors


def generate_triangles(limit):
    l = 1
    while l <= limit:
        yield sum(range(l + 1))
        l += 1

def test_triangles():
    triangles = generate_triangles(100000)
    for i in triangles:
        if get_factors(i) > 499:
            return i
        
print(test_triangles())