def fac (n):
    if n==1:
        return 1
    else:
         return n * fac(n-1)

def numofpaths (x, y):
    if x==0 or y==0:
        return 1
    else:
        return numofpaths(x, y-1) + numofpaths(x-1, y)
print(fac(2*20)/fac(20)**2)
print(numofpaths(4,4))
