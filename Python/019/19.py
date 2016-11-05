dayDictNum={'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6,
            'sunday':7}
dayDictDay={1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday',
            7:'sunday'}
monthDict={0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30,
           11:31}
monthDictLeap={0:31, 1:29, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30,
           11:31}

def countDown(num):
    while num>7:
        num-=7
    return num

SundayList=[]
# january 1 1900 was a monday, therefore:
day=countDown(1+365)
year=1901
while year<=2000:
    months=12
    if year%4==0 and year!=2000:
        for i in range(0, months):
            day=countDown(day)
            if dayDictNum['sunday']==day:
                SundayList.append(year)
            day+=monthDictLeap[i]
    else:
        for i in range(0, months):
                day=countDown(day)
                if dayDictNum['sunday']==day:
                    SundayList.append(year)
                day+=monthDict[i]
    year+=1
print(len(SundayList))
    
