import math
a = 2
b = 2
a_b = []

def exponential(base, power, storage):
    while power < 101:
        storage.append(math.pow(base, power))
        power += 1

    return storage

while a < 101:
    a_b = exponential(a, b, a_b)
    a += 1

print(len(set(a_b)))