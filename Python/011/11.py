f=open('datatexteuler10.txt','r')
x=f.read().split()
f.close
masterlist=[]
leftright=[]
rightleft=[]
updown=[]
rightdown=[]
leftdown=[]
rightup=[]
leftup=[]
productlist=[]
#____________________________________________________
for i in x:
    masterlist.append(int(i))
#____________________________________________________
c1=0
c2=1
c3=2
c4=3
limit=17
while c4<=399:
    leftright.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1+=1
    c2+=1
    c3+=1
    c4+=1
    if c1==limit:
        c1+=3
        c2+=3
        c3+=3
        c4+=3
        limit+=20
productlist.append(max(leftright))
#_________________________________________________________
c1=399
c2=398
c3=397
c4=396
limit=382
while c4>=0:
    rightleft.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1-=1
    c2-=1
    c3-=1
    c4-=1
    if c1==limit:
        c1-=3
        c2-=3
        c3-=3
        c4-=3
        limit-=20
productlist.append(max(rightleft))
#_________________________________________________________________
c1=0
c2=21
c3=42
c4=63
limit=17
while c4<=399:
    rightdown.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1+=1
    c2+=1
    c3+=1
    c4+=1
    if c1==limit:
        c1-=3
        c2-=3
        c3-=3
        c4-=3
        limit+=20
productlist.append(max(rightdown))
#_________________________________________________________________
c1=19
c2=38
c3=57
c4=76
limit=2
while c4<=399:
    leftdown.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1-=1
    c2-=1
    c3-=1
    c4-=1
    if c1==limit:
        c1+=37
        c2+=37
        c3+=37
        c4+=37
        limit+=20
productlist.append(max(leftdown))
#__________________________________________________________________
c1=399
c2=378
c3=357
c4=336
limit=382
while c4>=0:
    leftup.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1-=1
    c2-=1
    c3-=1
    c4-=1
    if c1==limit:
        c1-=3
        c2-=3
        c3-=3
        c4-=3
        limit-=20
productlist.append(max(leftup))
#_____________________________________________________________________
c1=380
c2=361
c3=342
c4=323
limit=397
while c4>=0:
    rightup.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1+=1
    c2+=1
    c3+=1
    c4+=1
    if c1==limit:
        c1-=37
        c2-=37
        c3-=37
        c4-=37
        limit-=20
productlist.append(max(rightup))
#__________________________________________________________________________
c1=0
c2=20
c3=40
c4=60
while c4<=399:
    updown.append(masterlist[c1]*masterlist[c2]*masterlist[c3]*masterlist[c4])
    c1+=1
    c2+=1
    c3+=1
    c4+=1
productlist.append(max(updown))
#__________________________________
print(max(productlist))

     
 
    




