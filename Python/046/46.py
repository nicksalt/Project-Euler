def isPrime(n):
    if n%2==0 or n%5==0:
        return False
    else:
        for i in range(3, int(n**.5)+1, 2):
            if n % i == 0:
                return False
    return True
def primes(num):
    lp = [2, 3, 5, 7, 11]
    candidate = 11
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
pl = primes(1000)

def findComp(primes):
    n=9
    done=False
    while not done:
        if not bS(primes, n):
            
