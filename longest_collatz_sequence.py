from typing import Dict

def collatz(n: int, d: Dict[int,int]) -> int:
    try:
        return d[n]
    
    except KeyError:
        if n % 2 == 0: # recurring if n is even
            d[n] = 1 + collatz(n //2, d)
        
        else: # recurring if n is odd
            d[n] = 1 + collatz(3*n + 1, d)
        
        return d[n]

def solve():
    upper = int(1e6)

    d = {1: 1}
    for i in range(1, upper):
        collatz(i, d)

    v = list(d.values())
    k = list(d.keys())
    ans = k[v.index(max(v))]

    print(ans)

solve()