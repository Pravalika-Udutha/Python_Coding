nums=[int(x) for x in input("Enter the values of list:").split()]
k=int(input("Enter the k value:"))
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if (nums[i]*nums[j])%k==0:
            count+=1
print(count)