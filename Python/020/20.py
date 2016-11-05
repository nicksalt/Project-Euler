#https://projecteuler.net/problem=20
n=100
counter=0
for i in range(1,100):
    n=n*i
n=str(n)
for i in n:
    counter=counter+int(i)
print(counter)
