n=0
a=0
while a==0:
    goal = int(input("Enter a number n, 1-1,000,000 to find the nth prime number."))
    primes = [2, 3, 5, 7]
    candidate = 11
    while goal >= len(primes):
        limit = candidate ** 0.5
        for p in primes:
            if p > limit:
                primes.append(candidate)
                break
            if candidate % p == 0:
                break
        candidate += 2

    print("Prime", str(goal), "is", str(primes[goal - 1]))
    print(sum(primes)-primes[goal])
    
        
## of Primes under 2,000,000 is 148933

    b=input('Would you like to continue?')
    if b=='yes':
        a=0
    else:
        a+=1
    

    
    

    
        
