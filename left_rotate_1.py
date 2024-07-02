#rotate the array by 1 position left
nums=[int(x) for x in input("enter the values:").split()]

temp=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]

nums[-1]=temp

print(nums)