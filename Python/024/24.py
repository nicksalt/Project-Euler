import itertools
from time import time
def main(list, target):
    start=time()
    l1=set(itertools.permutations(list))
    l2=[]
    for i in l1:
        x=''.join(i)
        l2.append(int(x))
    l2.sort()
    print(time()-start)
    return l2[target-1]

l=['0','1','2','3','4','5','6','7','8','9']
target=1000000
print(main(l, target))
