import itertools
templist=set(itertools.permutations(['0','1','2','3','4','5','6','7','8','9']))
pans=[''.join(i) for i in templist]
nums=[]
for i in pans:
    d1=int(i[1:4])
    d2=int(i[2:5])
    d3=int(i[3:6])
    d4=int(i[4:7])
    d5=int(i[5:8])
    d6=int(i[6:9])
    d7=int(i[7:])
    if d7%17==0:
        if d6%13==0:
            if d5%11==0:
                if d4%7==0:
                    if d3%5==0:
                        if d2%3==0:
                            if d1%2==0:
                                nums.append(int(i))
                                
print(sum(nums))                
