#rotate the array by 1 position right
nums=[int(x) for x in input("enter the values:").split()]

temp=nums[-1]
for i in range(len(nums)-1,0,-1):
    #print(i)
    nums[i]=nums[i-1]

nums[0]=temp

print(nums)