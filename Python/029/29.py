l=[]
for a in range(2, 101):
    for b in range(2,101):
        x=a**b
        l.append(x)
l.sort()
k=0
while k<len(l):
    if l.count(l[k])>1:
        del l[k]
    else:
        k+=1
print(len(l))
