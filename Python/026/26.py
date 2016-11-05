from decimal import *

def recurring():
    getcontext().prec = 2000
    num=7
    length=6
    for x in range(999,7,-2):
        n = str(Decimal(1)/x)[2:]
        l=len(n)
        if length>x or len(n)<1000:
            break;
        for i in range(1,l//2):
            i1=0
            i2=i
            l1=[]
            while i2<=(l):
                    l1.append(n[i1:i2])
                    i1+=i
                    i2+=i
            if l1.count(l1[0]) == len(l1):
                if len(l1[0])>length:
                        length = len(l1[0])
                        num = x
                        break
    return num

                        
        
    

    
