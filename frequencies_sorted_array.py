my_list=[int(x) for x in input("Enter the values:").split()]

curr=None
count=0
for x in my_list:
    if curr!=x:
        curr=x
        count+=1
    else:
        count+=1
    print(x,count)