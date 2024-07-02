my_list=[eval(x) for x in input("Enter the numbers:").split()]
second=0
first=0
if my_list[0]>my_list[1]:
    second=my_list[1]
    first=my_list[0]

for i in my_list:
    if i>first:
        second=first
        first=i
    if i>second and i!=first:
        second=i

print(f"The second largest number in list is {second}")