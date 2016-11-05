import math
from time import time
abundantList=[]
sums=[]
nonsums=0
def findAbundant(num):
    list=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            list.append(i)
    end=len(list)
    for i in range (1, end):
        check=int(num/list[i])
        if check not in list:
            list.append(check)
    if sum(list)>num:
        return True
    else:
        return False

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
            if left[cleft]< right[cright]:#compares item from each list
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

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

start=time()
for i in range(12, 20161):
    if findAbundant(i)==True:
        abundantList.append(i)
for i in abundantList:
    for x in abundantList:
        if x>20161-i:
            break
        check=i+x
        if not binarySearch(sums,check):
            sums.append(check)
sums=mergeSort(sums)
for i in range(2, 20161, 2):
        if not binarySearch(sums, i):
            nonsums+=i
end=time()
print(nonsums)
print(end-start, 'secs')
