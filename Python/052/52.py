done=False
x=101
while not done:
    templist=[i for i in str(x)]
    templist2=[i for i in str(x*2)]
    templist.sort()
    templist2.sort()
    if templist==templist2:
        templist3=[i for i in str(x*3)]
        templist3.sort()
        if templist==templist3:
            templist4=[i for i in str(x*4)]
            templist4.sort()
            if templist==templist4:
                templist5=[i for i in str(x*5)]
                templist5.sort()
                if templist==templist5:
                    templist6=[i for i in str(x*6)]
                    templist6.sort()
                    print(templist6, templist)
                    if templist==templist6:
                        print(x)
                        done=True
    x+=1
