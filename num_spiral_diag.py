num = 1 # this will be the final number after each iteration
count = 1
d = 2 # this is the difference; add 2 to this after every 4 iterations
sample = [1]
total = 1

for count in range(1, 501):
    i = 1
    while i <= 4:
        num += d
        i += 1
        total += num

    d += 2
print(total)