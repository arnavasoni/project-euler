fact = {1:1}
for i in range(2, 10001):
    facts = []
    for j in range(1, i):
        if i%j == 0:
            facts.append(j)
    fact[i] = sum(facts)

sum = 0
for key in fact:
    value = fact[key]
    if value in fact.keys():
        if key == fact[value] and value == fact[key] and value != key:
            sum += key
    else:
        continue

print(sum)
