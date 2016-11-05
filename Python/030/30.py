def powers(power):
    limit=9**power*(power*10)
    nums=[]
    for i in range(10, limit):
        s=0
        for x in str(i):
            s+=int(x)**power
        if s==i:
            nums.append(i)
    print(nums)
    return sum(nums)
print(powers(5))
