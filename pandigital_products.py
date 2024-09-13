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