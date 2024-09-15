def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_rotations(num):
    rotations = []
    str_num = str(num)
    for i in range(len(str_num)):
        rotation = str_num[i:] + str_num[:i]
        rotations.append(int(rotation))
    return rotations

count = 0
for i in range(2, 1000000):  # Adjust range as needed
    rotations = get_rotations(i)
    if all(is_prime(rot) for rot in rotations):
        count += 1

print(count)
