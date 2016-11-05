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
    return lp[:len(lp)-1]

a=primes(1000000)
b=a[3:24]
print(b)
print(sum(b))
