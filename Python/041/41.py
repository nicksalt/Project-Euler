import itertools
def primes(n):
    if n%5==0 or n%2==0:
        return False
    else:
        limit=int(n**.5)
        for i in range(2, limit):
            if n%i==0:
                return False
    return True
            
l=['1','2','3','4','5','6','7','8','9']
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
master=[]
for i in set(itertools.permutations(l[:5])):
    l5.append(int(''.join(i)))
for i in set(itertools.permutations(l[:6])):
    l6.append(int(''.join(i)))
for i in set(itertools.permutations(l[:7])):
    l7.append(int(''.join(i)))
for i in set(itertools.permutations(l[:8])):
    l8.append(int(''.join(i)))
for i in set(itertools.permutations(l[:11])):
    l9.append(int(''.join(i)))
l5.sort()
l6.sort()
l7.sort()
l8.sort()
l9.sort()
print('done')
master.extend([l5,l6,l7,l8,l9])
print(master[0])
for i in range(len(master)-1, -1, -1):
    list=master[i]
    for  x in range(len(list)-1, -1, -1):
        if primes(list[x]):
            print(list[x])
            quit()
        

