prodpal_max = 1
i = 1000
while i > 99:
    j = 1000
    while j > 99:
        prod = i*j
        if prod > prodpal_max and str(prod) == str(prod)[-1::-1]:
            prodpal_max = prod
        j -= 1
    i -= 1

print(prodpal_max)