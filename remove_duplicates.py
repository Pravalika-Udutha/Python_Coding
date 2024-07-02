#removing duplicates from the sorted list
my_list=[int(x) for x in input("Enter the values:").split()]
i=0
j=1

while j<len(my_list):
    if my_list[j]!=my_list[i]:
        i+=1
        my_list[i]=my_list[j]
    j+=1

my_list=my_list[:i+1]

print(my_list)