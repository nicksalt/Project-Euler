l=[0,1,2,3,4,5,6,7,8,9]
def fac(num):
    if num==1:
        return 1
    else:
        return num*fac(num-1)
                                       
total=fac(len(l))
target=1000000
digetlist=[]
for i in range(1,9):
    if total*i/9>target:
        digetlist.append(i-1)
        

