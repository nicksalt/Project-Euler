f=open('18.txt','r')
l=f.read().split('\n')
f.close()


def SortList(list):
    numList=[]
    for i in list:
        tempList=[]
        if len (i) <=2:
            tempList.append(int(i))
        else:
            j=0
            k=1
            while k<=len(i)-1:
                tempNum=i[j]+i[k]
                tempList.append(int(tempNum))
                j+=3
                k+=3
        numList.append(tempList)
    return numList 


def AddPaths(list):
    for i in range (len(list)-2, -1, -1):
        targetLine=list[i]
        for num in range(0, len(targetLine)):
            targetNum=targetLine[num]
            checkNums=list[i+1][num:num+2]
            list[i][num]=targetNum+max(checkNums)
    return list[0]

print(AddPaths(SortList(l)))
        
              

