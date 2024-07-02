#seperating the even and odd numbers from a given list
total_list=[int(x) for x in input("Enter the numbers:").split()]
even_list=[]
odd_list=[]
for i in total_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"The even list from given list is {even_list}\nThe odd list from given list is {odd_list}")