import math

def is_prime(n):
    s=True
    sqr=int(math.sqrt(n))
    

    for j in range(2,sqr+1):
        if n%j==0:return False
    return s
             

T=int(input())
            
for i in range (T):
    n= int(input())
    if n==1 or ((n!=2) and (n%2==0)):print("Not prime")
    elif (n==2) or (is_prime(n)):print("Prime")
    else:print("Not prime")
        
