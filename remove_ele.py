nums=[int(x) for x in input("Enter the values:").split()]
val=int(input("Enter the value:"))
count=0
temp=0
nums1=[]
for i in range(len(nums)):
    
    if nums[i]!=val:
        nums1[temp]=nums[i]
        temp+=1
        count+=1
    

print(count)
