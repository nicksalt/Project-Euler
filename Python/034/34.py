from time import time
def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)
l=[]
dic={0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880, 10:3628800}
start=time()
for i in range(3, 9999999,2):#9999999-7*9!>0
    sums=0
    for x in str(i):
        sums+=dic[int(x)]
    if sums==i:
        l.append(int(i))
        print(len(l))
print(time()-start)
print(sum(l))
