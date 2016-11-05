f=open('22.txt','r')
l=f.read().split(',')
f.close()
scoring={'A':1, 'B':2, 'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
         'Q':17,'R':18,'S':19,'T':20,'U':21, 'V':22,'W':23,'X':24,'Y':25,'Z':26}
def mergeSort(list):
    if len(list)>1:
        mid = len(list)//2#calculates a rounded value for mid
        left = list[:mid]#splits list in half into two different list
        right = list[mid:]
        mergeSort(left)#runs the function untill the length of the list is equal to one
        mergeSort(right)
        cleft=0#counterleft
        cright=0
        ctotal=0
        while cleft < len(left) and cright < len(right):
            if left[cleft].lower() < right[cright].lower():#compares item from each list
                list[ctotal]=left[cleft]#Inputs the object in the left list into the whole list
                cleft+=1
            else:
                list[ctotal]=right[cright]
                cright=cright+1
            ctotal+=1
            
        while cleft < len(left):
            list[ctotal]=left[cleft]
            cleft=cleft+1
            ctotal+=1

        while cright < len(right):
            list[ctotal]=right[cright]
            cright=cright+1
            ctotal=ctotal+1
    return list
sortedList=mergeSort(l)
scores=[]
for i in range(0, len(sortedList)):
    name=sortedList[i]
    position=i+1
    score=0
    for i in name:
        if i in scoring:
            score+=scoring[i]
    score=score*position
    scores.append(score)
print(sum(scores))
        
