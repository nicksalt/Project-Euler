def primes(num):
    list=[2,3,5,7]
    candidate=11
    while list[len(list)-1] < num:
        limit = candidate ** 0.5
        for p in list:
            if p > limit:
                list.append(candidate)
                break
            if candidate % p == 0:
                break
        candidate += 2
    return list[:len(list)-1]

def isprime(num):
    if num%2==0 or num%5==0:
        return False
    limit =int( num**.5)+1
    for i in range(3, limit, 2):
        if num%i==0:
            return False
    return True

maxn=0
prod=0
blist=primes(1000)
print(blist)
for a in range(1, 1000):
    for b in blist:
        n=0
        done = False
        while not done:
            candidate=(n**2)+(a*n)+(b)
            if isprime(abs(candidate)):
                n+=1
            else:
                if n>maxn:
                    maxn=n
                    prod=a*b
                    print(maxn, a, b)
                    
                done=True

for a in range(1, 1000):
    for b in blist:
        n=0
        done = False
        while not done:
            candidate=(n**2)-(a*n)+(b)
            if isprime(abs(candidate)):
                n+=1
            else:
                if n>maxn:
                    maxn=n
                    prod=-a*b
                    print(maxn, -a, b)
                done=True
for a in range(1, 1000):
    for b in blist:
        n=0
        done = False
        while not done:
            candidate=(n**2)+(a*n)-(b)
            if isprime(abs(candidate)):
                n+=1
            else:
                if n>maxn:
                    maxn=n
                    prod=a*-b
                    print(maxn, a, -b)
                done=True
for a in range(1, 1000):
    for b in blist:
        n=0
        done = False
        while not done:
            candidate=(n**2)-(a*n)-(b)
            if isprime(abs(candidate)):
                n+=1
            else:
                if n>maxn:
                    maxn=n
                    prod=-a*-b
                    print(maxn, -a, -b)
                done=True
                

print(prod)
print(maxn)
