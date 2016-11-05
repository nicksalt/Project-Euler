import math
solutions=[]
for d in range(2,10):
    for n in range(1,d):
        frac=n/d
        tempd=str(d)
        tempn=str(n)
        temp=[]
        for i in range(1,10):
            tempd1=str(i)+tempd
            tempn1=str(i)+tempn
            tempd2=tempd+str(i)
            tempn2=tempn+str(i)
            if frac==(int(tempn2)/int(tempd1)):
                solutions.append(frac)
  
                                
prod=float(1.0)
for i in solutions:
    prod*=float(i)
print(round(1/prod))
