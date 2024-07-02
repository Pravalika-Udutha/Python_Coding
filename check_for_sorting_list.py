my_list=[eval(x) for x in input("enter the numbers:").split()]
minimum=0
maximum=0

if my_list[0]<my_list[1]:
#ascending order
    minimum=my_list[0]
    for i in my_list:
        if i<minimum:
            print("The list is not sorted")
            break
        else:
            minimum=i
            x=len(my_list)
else:
    maximum=my_list[0]
    #descending order
    for i in my_list:
        if i>maximum:
            print("The list is not sorted")
            break
        else:
            maximum=i
            x=len(my_list)
            
if my_list[x-1]==minimum or my_list[x-1]==maximum:
    print("The list is sorted")
#we can execute the program by using all function also