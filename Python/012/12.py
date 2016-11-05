import time
start=time.time()
for i in range(1000,999999999):
    n=int(i*(i+1))/2
    c=0
    for i in range(1, i+1):
        if i%n==0:
            c+=1
        if c==500:
            print(i)
            break
end=time.time()
print(end-start, 'seconds')
