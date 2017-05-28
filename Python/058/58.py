def isprime(num):
    if num%2==0 or num%5==0:
        return False
    limit =int( num**.5)+1
    for i in range(3, limit, 2):
        if num%i==0:
            return False
    return True

def main():
    side = 9
    last_num = 49
    primes = 8
    total = 13
    below_ten_percent = False
    while not below_ten_percent:
        diagonals = [last_num + side - 1, last_num + 2*side - 2,
                     last_num + 3*side - 3, last_num + 4*side - 4]
        last_num = diagonals[3]
        total += 4
        for i in diagonals:
            if isprime(i):
                primes += 1
        if primes/float(total) < 0.1:
            below_ten_percent = True
        else:
            side += 2
    print(side)

main()