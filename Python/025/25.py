

def fibfunc(numofdigits):
    list=[1,1,2]
    if numofdigits==1:
        return list[0]
    if numofdigits>1:
        counter=1
        while len(str(list[len(list)-1]))<numofdigits:
            nextfib=list[counter]+list[counter+1]
            list.append(nextfib)
            counter+=1
        return len(list)

print(fibfunc(1000))

