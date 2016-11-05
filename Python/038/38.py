from time import time
#my original code
target=['1','2','3','4','5','6','7','8','9']
l=len(target)
prods=[]
ns=[]
start=time()
for i in range(1,9876):
    done=False
    n=1
    temp=[]
    while not done:
        prod=i*n
        temp+=[i for i in str(prod)]
        if len(temp)>l:
            done=True
        if len(temp)==l:
            prod=int(''.join(temp))
            temp.sort()
            if temp==target:
                prods.append(prod)
                ns.append(i)
                done=True
        n+=1
print(max(prods))
print(time()-start)               
#faster solution
def find(target):
    for i in range(9876, 8, -1):
        done=False
        n=1
        temp=[]
        while not done:
            prod=i*n
            temp+=[i for i in str(prod)]
            if len(temp)>l:
                done=True
            if len(temp)==l:
                prod=int(''.join(temp))
                temp.sort()
                if temp==target:
                    return(prod)
            n+=1
start=time()
print(find(target))
print(time()-start)
