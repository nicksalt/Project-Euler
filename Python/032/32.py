target=['1','2','3','4','5','6','7','8','9']
prods=[]
al=[]
bl=[]

for a in range(1, 9876):
    for b in range(1,999):
        c=a*b
        temp=[i for i in str(a)]+[i for i in str(b)] +[i for i in str(c)]
        temp.sort()
        if temp==target:
            if c not in prods:
                prods.append(c)
                al.append(a)
                bl.append(b)
print(al,bl,prods)
