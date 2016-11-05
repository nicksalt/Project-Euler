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

def max_sequence(lst):
    for i in range (len(lst)):
        temp=sum(lst[i:])
        if temp< 1000000:
            if is_prime(temp):
                return(len(lst[i:]), temp)
def under_mill(n, lst, m):
    temp=lst[len(lst)-1]
    while sum(lst)>n:
        temp=lst[len(lst)-1]
        del lst[len(lst)-1]
    lst.append(temp)
    while sum(lst)>n:
        del lst[0]
    if sum(lst)==n and len(lst)>m:
        return n
    return False
        
    
def find_prime():
    primelst=primes(4481, [2,3])
    temp=max_sequence(primelst[::-1])
    m=temp[0]
    n=temp[1]
    l=primes(1000000, [n])[::-1]
    for i in l:
        temp=primelst[:]
        if under_mill(i, temp, m)!=False:
            return i
    return n

