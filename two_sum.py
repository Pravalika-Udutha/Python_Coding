nums=[int(x) for x in input("Enter the values of list:").split()]
target=int(input("Enter the target value:"))
opt=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            opt.append(i)
            opt.append(j)
            
    
print(opt[0:2])