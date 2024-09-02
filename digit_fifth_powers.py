def digits_sum(num):
    digits = []
    while num != 0:
        digits.append(num%10)
        num //= 10
    digit_5 = lambda x: x**5
    digits = [digit_5(x) for x in digits]
    # digits = [lambda x: x**5 for x in digits]
    # print(digits, sum(digits))
    digits_sum = sum(digits)
    return digits_sum


total = 0
for i in range(2, 7*(9**5)):
    digits_total = digits_sum(i)
    if digits_total == i:
        total += i

print(total)
# digits_total = digits_sum(12345)