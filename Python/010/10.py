def sum_primes(limit):
    primes = []
    for n in range(2, limit+1):
        for p in primes:
            if n % p == 0: break     
            if n < p*p:
               primes.append(n)      
               break
        else: primes.append(n)       
    return sum(primes)
a=int(input(''))
sum_primes(a)
