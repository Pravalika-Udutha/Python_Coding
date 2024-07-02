#finding the averages of list elements

sample_list=[eval(x) for x in input("Enter the list elements:").split()]
sum_of_numbers=0
count=0
for i in sample_list:
    count+=1
    sum_of_numbers+=i

print(f"The average of {sample_list} is {sum_of_numbers/count}")