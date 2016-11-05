m=2
n=600851475143
 
while m<=n:
    m+=1
    if n%m==0:
        n =n/m
        if n!=1:
            m=2

print(m)
