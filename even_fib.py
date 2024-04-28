f, s = 1, 2
sum_even = 0
while f < 4*10**6:
    if f % 2 == 0:
        sum_even += f

    f, s = s, f+s

print(sum_even)