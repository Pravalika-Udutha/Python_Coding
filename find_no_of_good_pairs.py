nums1=[int(x) for x in input("Enter the values of list1:").split()]
nums2=[int(x) for x in input("Enter the values of list2:").split()]
k=int(input("Enter the k value:"))
count=0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]%(nums2[j]*k)==0:
            count+=1
            print(f"{i,j}")

print(f"The good pairs are {count} in number")