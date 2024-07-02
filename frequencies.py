#finding the frequency of each element in a sorted array
nums=[int(x) for x in input("Enter the values of list:").split()]
freq=1
for i in range(1,len(nums)):
    
    if nums[i]==nums[i-1]:
        freq+=1
    else:
        print(nums[i-1],freq)
        freq=1
        

print(nums[-1],freq)
