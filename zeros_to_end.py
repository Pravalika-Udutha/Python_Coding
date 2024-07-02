my_list=[int(x) for x in input("Enter the values of list:").split()]

for i in range(len(my_list)):
    if my_list[i]==0:
        
        for j in range(i+1,len(my_list)):
            if my_list[j]!=0:
                my_list[i]=my_list[j]
                my_list[j]=0
                break
        
        
    

print(my_list)