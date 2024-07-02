#using linear searching strategy to find the element in list or not
def linear_search(my_list,key):
    #code for searching
    for i in range(len(my_list)):
        if my_list[i]==key:
            return i
    return -1
            

#reading data from user
my_list=[int(x) for x in input("Enter the values to list:").split()]
key=int(input("Enter the value to find:"))
found=linear_search(my_list,key)
if found==-1:
    print(f"{key} is not found")
else:
    print(f"{key} is found at {found} index")