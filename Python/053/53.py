from time import time
from math import factorial

def main():
    start=time()
    check=0
    for n in range(1,101):
        for r in range(1,n+1):
            if factorial(n)/(factorial(r)*factorial(n-r)) > 1000000:
                check+=1
    end=time()
    return check, end-start
            
