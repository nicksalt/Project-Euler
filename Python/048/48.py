num=0
for i in range(1,1001):
    num+=(i**i)
num=str(num)
print(num[(len(num)-10):])
