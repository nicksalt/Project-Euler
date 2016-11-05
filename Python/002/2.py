#https://projecteuler.net/problem=2
l1=[1,2]
c1=0
c2=1
counter=0

while (l1[c1]+l1[c2])<4000000:
    l1.append(l1[c1]+l1[c2])
    c1+=1
    c2+=1
for i in l1:
    if i%2==0:
        counter=counter+i
print(counter)

