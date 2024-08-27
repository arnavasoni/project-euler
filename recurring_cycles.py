def repeating_cycle(denom :int, num :int=1)->int:
    '''We will do long division method but we will be tracking the reminder throught the division
    The reason for doing it is sometime the the number in quotient might repeat even though it is part of 
    full cycle. e.g. 1/17 = 0.(0588235294117647) if we were to only look at quotient then 8 is repeted just at the 4th place but our
    actual cycle is of 16 digits.And this is very well known in maths'''

    reminders = []
    rems = None
    while rems not in reminders:
        reminders.append(rems)
        num *= 10
        rems = num % denom

    reminders.pop(0)
    return len(reminders)

opt = []
for i in range(1, 1000):
    opt.append(repeating_cycle(i))

print(opt.index(max(opt))+1)