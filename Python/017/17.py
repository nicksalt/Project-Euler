import time
start=time.time()
letters=0
for i in range(1,1001):
    while i>0:
        if len(str(i))==1:
            if i==1:
                letters+=3
            if i==2:
                letters+=3
            if i==3:
                letters+=5
            if i==4:
                letters+=4
            if i==5:
                letters+=4
            if i==6:
                letters+=3
            if i==7:
                letters+=5
            if i==8:
                letters+=5
            if i==9:
                letters+=4
            i=0
        if len(str(i))==2:
            if 10<=i<=20:
                if i==10:
                    letters+=3
                if i==11:
                    letters+=6
                if i==12:
                    letters+=6
                if i==13:
                    letters+=8
                if i==14:
                    letters+=8
                if i==15:
                    letters+=7
                if i==16:
                    letters+=7
                if i==17:
                    letters+=9
                if i==18:
                    letters +=8
                if i==19:
                    letters+=8
                i=0
            else:
                if str(i)[0]==2:
                    letters+=6
                if str(i)[0]==3:
                    letters+=6 
                if str(i)[0]==4:
                    letters+=5
                if str(i)[0]==5: 
                    letters+=5
                if str(i)[0]==6: 
                    letters+=5
                if str(i)[0]==7: 
                    letters+=7
                if str(i)[0]==8:  
                    letters+=6
                if str(i)[0]==9:
                    letters+=5
                i=int(str(i)[1:])
        if len(str(i))==3:
            if str(i)[0]==1:
                letters+=13
            if str(i)[0]==2: 
                letters+=13
            if str(i)[0]==3:
                letters+=15
            if str(i)[0]==4:
                letters+=14
            if str(i)[0]==5: 
                letters+=14
            if str(i)[0]==6: 
                letters+=13
            if str(i)[0]==7: 
                letters+=15
            if str(i)[0]==8:  
                letters+=15
            if str(i)[0]==9:
                letters+=14
            i=int(str(i)[1:])
        if len(str(i))==4:
            letters+=11
            i=0
letters-=(9*3)
print(letters)
end=time.time()
print(end-start, 'seconds')
