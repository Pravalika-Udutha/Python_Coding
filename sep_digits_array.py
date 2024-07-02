my_list=[int(x) for x in input("Enter the values:").split()]
new_list=[]
for i in range(len(my_list)-1,-1,-1):
    while my_list[i]>0:
        temp=my_list[i]%10
        new_list.append(temp)
        my_list[i]//=10
new_list.reverse()
print(new_list)