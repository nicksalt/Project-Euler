from itertools import permutations
from functools import reduce
from time import time

def primes(goal, primes):
    candidate = primes[len(primes)-1]+2
    while goal > primes[len(primes)-1]:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 2
    return primes
def is_prime(n):
    factors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    if len(factors)==2:
        return True
    return False
    
l=[1009,1013]
goal=10000
primes=primes(goal, l)
data=[]
start=time()
for prime in primes:
    check=[]
    primelst=list(str(prime))
    if primelst.count('0')<2:
        perm=set(permutations(primelst))
        for n in perm:
            n=''.join(n)
            if len(str(int(n)))==4:
                if is_prime(int(n)) and int(n)!=prime:
                    check.append(n)
    if len(check)>=3:
        check.sort()
        for first in range(len(check)):
            for second in range(first+1, len(check)):
                if int(check[first])-prime==int(check[second])-int(check[first])==3330:
                    ans=str(prime)+str(check[first])+str(check[second])
                    if '1487' not in ans:
                        print(ans)
end=time()
print(end-start)
