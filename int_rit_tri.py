import numpy as np

def is_right_tri(a, b, c):
    return a**2 + b**2 == c**2

solution_count = np.zeros(1001)

for p in range(1, 1001): # perimeter from 1 to 1000
    for a in range(1, p//2): # can go from 1 to i/2
        for b in range(a, (p-a)//2): # k can go from j to (i-j)/2
            c = p-a-b
            if is_right_tri(a, b, c):
                solution_count[p] += 1

max_solutions_perimeter = np.argmax(solution_count)
print(max_solutions_perimeter)