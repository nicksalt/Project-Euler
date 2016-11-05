import math, functools
def isPrime(num):
    if num%2==0 or num%5==0 or num==1:
        return False
    else:
        for i in range(3, int(math.sqrt(num))+1):
            if num%i==0:
                return False
    return True
def findFactor(n):
    return set(functools.reduce(list.__add__, ([i, n//i]
                                               for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))
   
  
def find():
    c=0
    n=1000
    while True:
        l=[]
        facts=findFactor(n)
        for fact in facts:
            if isPrime(fact):
                l.append(fact)
        if len(l)==4:
            c+=1
            if len(str(n))>5:
                print(n)
        else:
            c=0
        if c==3:
            return n-2
        n+=1
print(find())
        
