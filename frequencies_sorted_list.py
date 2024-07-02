#Finding the frequencies in a sorted list
# Input:  arr[] = {2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6}
my_list=[int(x) for x in input("Enter the values:").split(",")]
count=1
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)-1):
        if my_list[i]==my_list[j]:
            count+=1
        else:
            i+=1
    print(f"The element {my_list[i]} occurs in {count} times")