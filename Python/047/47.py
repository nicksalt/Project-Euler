from functools import reduce
from time import time
def primes(goal, primes):
    candidate = primes[len(primes)-1]+2
    while goal > primes[len(primes)-1]:
        limit = candidate ** 0.5
        for p in primes:
            if p > limit:
                primes.append(candidate)
                break
            if candidate % p == 0:
                break
        candidate += 2
    return primes

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def prime_factors(primes,total,n,time):
    for i in primes:
        if (n/i)%i==0:
            i=int(n/i/i)
        if i not in total:
            total.append(i)
    if len(total)==4*time:
        return total
    return False
	    
def main():
    primelst=[2,3,5,7]
    n=645
    start=time()
    while True:
        total=[]
        primelst=primes(int(n/2)+4, primelst)
        fac=factors(n).intersection(primelst)
        total=prime_factors(fac,total,n,1)
        if total!=False:
            fac=factors(n+1).intersection(primelst)
            total=prime_factors(fac,total,n+1,2)
            if total!=False:
                fac=factors(n+2).intersection(primelst)
                total=prime_factors(fac,total,n+2,3)
                if total!=False:
                    fac=factors(n+3).intersection(primelst)
                    total=prime_factors(fac,total,n+3,4)
                    if total!=False:
                        end=time()
                        print(end-start)
                        return n
  
        n+=1
                                    
                
        
        
