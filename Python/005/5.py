maxNum=20
numbers=[]
for i in range(2,maxNum+1):
    numbers.append(i)
print(numbers)

denominators=[]
for i in range(len(numbers)):
    n=numbers[i]
    if n==1: continue
    for j in range(i,len(numbers)):
        if numbers[j] % n ==0:
            numbers[j]=numbers[j] // n
    denominators.append(n)
    print(numbers, '=>', denominators)
    
prod=1
for i in denominators:
    prod*=i
print('product = ', prod)
