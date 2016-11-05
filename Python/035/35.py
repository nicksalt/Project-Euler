from time import time
import itertools, math
def primes(num):
    lp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    candidate = 101
    while num > lp[len(lp)-1]:
        limit = candidate ** 0.5
        for p in lp:
            if p > limit:
                lp.append(candidate)
                break
            if candidate % p == 0:
                break
        candidate += 2
    return lp[25:len(lp)-1]
def shift(l, n):
    return l[n:] + l[:n]
def bS(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
def cirCheck(n):
    l=[]
    num=str(n)
    primes=0
    combos=len(num)
    for i in num:
        l.append(i)
    for i in range(0, combos):
        templist=shift(l, i)
        num=int(''.join(templist))
        if bS(candidates, num):
            primes+=1
    if primes==combos:
        return True
    return False
    


cp=[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
candidates=primes(1000000)
start=time()
for i in candidates:
    if cirCheck(i):
        cp.append(i)
print(time()-start)
print(len(cp))
    

    
