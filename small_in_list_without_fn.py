#finding the smallest element in list without using min()
my_list=[eval(x) for x in input("Enter the numbers:").split()]

minimum=my_list[0]
maximum=my_list[0]
for i in my_list:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i

print(f"The smallest element in list is {minimum}\nThe largest element in list is {maximum}") 