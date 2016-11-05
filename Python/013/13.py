#https://projecteuler.net/problem=13
f=open('DATA1.txt','r')
x=f.read().split()
f.close()
l1=[]
for i in x:
    l1.append(int(i))

a=str(sum(l1))
print(a[:10])

