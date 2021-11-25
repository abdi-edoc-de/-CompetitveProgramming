import math as math

def oneBase(n):
    ones = 0
    n = abs(n)
    while n >= 1 :
        upper = len(str(n)) + 1
        below = upper - 1
        upperOnes = int('1' * upper)
        belowOnes = int('1' * below) 
        
        if n < belowOnes:
            
            upper -= 1
            below -= 1
        upperOnes = int('1' * upper)
        belowOnes = int('1' * below) 
        
        upperDif = upperOnes - n
        belowDif = n - belowOnes
        if upperDif < belowDif:
            ones += (upper)
            n =  upperOnes - n
            # print(n,upper,ones,n//upperOnes,upperOnes,n,temp)
            
        else:
            temp = (n//belowOnes)
            ones +=( temp * below)
            n = n - ( temp * belowOnes) 
    print(ones)
def main():
    oneBase(int(input()))
main()

