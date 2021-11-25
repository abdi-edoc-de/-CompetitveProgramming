from math import log10
def recurse(n):
    print(n)
    if n == 1:
        return 1
    
    s = int(log10(n)) + 1
    ones = int("1" * s)
    m = n // ones
    # if(m * ones == n):
    #     return m * s
        
    above = (m + 1) * ones
    below = (m) * ones
    if m == 0:
        ones = int("1" * (s - 1))
        below = (9) * ones
    
    belowCost = sum([int(i) for i in str(below)])
    aboveCost = sum([int(i) for i in str(above)])

    belows = belowCost + recurse(n - below)
    aboves = aboveCost + recurse(above - n)
    
    print(n,below,above)
    print(n,belows,aboves)    
    return min(belows,aboves)

     
    

def solve(n):
    print(recurse(n))

def main():
    n = int(input())
    solve(n)

main()
# ans = recurse(1021)
# # ans = recurse(124534334343231)
# print(ans)