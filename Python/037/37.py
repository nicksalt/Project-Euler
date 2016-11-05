from time import time
def primes(nth):
    lp = [2,3,5,7]
    candidate = 11
    while nth > len(lp):
        limit = candidate ** 0.5
        for p in lp:
            if p > limit:
                lp.append(candidate)
                break
            if candidate % p == 0:
                break
        candidate += 2
    return lp
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

def check(num, list):
        num=str(num)
        x=len(num)
        combos=x*2-2
        primes=0
        for p in range(1,x):
            n1=num[p:]
            n2=num[:x-p]
            if bS(list, int(n1)) and bS(list, int(n2)):
                primes+=2
            else:
                return False
        if primes==combos:
            return True
        return False
start=time()
primes=primes(100000)
candidates=primes[4:]
nums=[]           
for i in candidates:
    if len(nums)<11:
        if check(i, primes):
            nums.append(i)
    else:
        break
print(time()-start)
print(sum(nums))
