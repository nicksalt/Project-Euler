num=0
solutions=0
for p in range(120, 1001):
    templist=[]
    for b in range(1, p):
        a=p*((p-2*b)/(2*(p-b)))
        if int(a)==a and a>0:
            if a+b not in templist:
                templist.append(a+b)
    if len(templist)>solutions:
        solutions=len(templist)
        num=p
print(num, solutions)
            
