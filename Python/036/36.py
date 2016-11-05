nums=[]
for i in range(1, 1000000):
    x=str(i)
    y=str(bin(i))[2:]
    if x==x[::-1] and y==y[::-1]:
        nums.append(i)
print(len(nums))
print(nums)
print(sum(nums))
