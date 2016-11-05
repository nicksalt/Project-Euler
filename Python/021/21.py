import math
def amicable(num):
    list=[]
    for i in range(1, int(math.sqrt(num)+1)):
        if num%i==0:
            list.append(i)
    end=len(list)
    for i in range (1, end):
        list.append(num/list[i])
    

amicable(284)
                   
