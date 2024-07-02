# Input:  arr[] = {16, 17, 4, 3, 5, 2}
# Output: leaders are 17, 5, 2
my_list=[int(x) for x in input("Enter the values:").split()]
maximum=my_list[-1]
list1=[]
list1.append(maximum)
for i in range(len(my_list)-1,-1,-1):
    if maximum<my_list[i]:
        list1.append(my_list[i]) 
        maximum=my_list[i]

list1.reverse()
print(list1)