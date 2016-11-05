x=500
nums=[1,3,5,7,9]
n1=nums[1]
n2=nums[2]
n3=nums[3]
n4=nums[4]
for i in range(1, x):
    n1+=8*i+2
    n2+=8*i+4
    n3+=8*i+6
    n4+=8*i+8
    nums.extend([n1,n2,n3,n4])
print(sum(nums))
