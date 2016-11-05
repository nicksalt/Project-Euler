from time import time
done=False
n=145
start=time()
while not done:
    if n%1000==0:
        print(n)
    h=n*(2*n-1)
    p=0
    temp=n+2
    while p<h:
        p=temp*(temp*3-1)/2
        if p==h:
            done=True
        else:
            temp+=2
    n+=2
end=time()
print( end-start, 'seconds \n')
print(h)
