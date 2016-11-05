l1=[]
counter=0
for i in range(1,1000):
    if i%3==i%5==0:
        l1.append(i)
    elif i%3==0:
        l1.append(i)
    elif i%5==0:
        l1.append(i)
for i in l1:
    counter=counter+i
print(counter)
print(l1)

    
    
