'''
Here are a few observations:
The number of digits of a,b,c combined must be equal to 10.
The term multiplicand (a) and the multiplier (b) are replaceable, i.e., a * b = c and b * a = c. So, while looking for desired combinations of multipliers and multiplicand, both (a, b) and (b, a) will satisfy the condition. However, we have to count them only once as they are practically the same.

Table
The columns represent the number of digits in b in the tables below. The rows show the number of digits in a, and the value in each cell represents the possible number of digits of c.
In the table below, there are four highlighted cases. However, this is because the multiplier and multiplicand are replaceable. Thus, we will consider the purple-highlighted cases as two and also as the only possible cases in which the number of digits of a,b,c combined could be equal to 10.

The first case:

a is double digit, b is triple digit, and c should be 5-digit.
The maximum possible double digit number is: a = 98 and the maximum possible 3-digit number is: b = 987.
Thus, the upper bound will be a=98 and b=987.

The second case:

a is a single digit, b is 4-digit, and c should be 5-digit.
The maximum possible single digit is a = 9. The maximum possible 4-digit b = 9876.
Thus, the upper bound will be a=9 and b=9876.
'''

sumC = 0
alreadyFound=[]

# CASE 1. (a - 2-digit) and (b - 3-digit) 
upperA = 98
upperB = 987
for a in range(9,upperA+1):
    for b in range(98,upperB+1):
        c = a*b
        if len(str(c))>5: break
        
        allDigits = sorted(str(c)+str(a)+str(b))
    
        if allDigits == list('123456789') :
            if c not in alreadyFound :
                alreadyFound+=[c]
                sumC+=c


# CASE 2. (a - 1-digit) and (b - 4-digit) 
upperA = 9
upperB = 9876
for a in range(1,upperA+1):
    for b in range(987,upperB+1):

        c = a*b
        if len(str(c))>5: break
        
        allDigits = sorted(str(c)+str(a)+str(b))
    
        if allDigits == list('123456789') :
            if c not in alreadyFound :
                alreadyFound+=[c]
                sumC+=c


print(sumC)