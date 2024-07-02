#reversing a list 
#it can be donr in various ways
#1.slicing  2.reverse() 3.loops
my_list=[int(x) for x in input("Enter the list elements:").split()]

i=0
j=len(my_list)-1

while i<=j:
    temp=my_list[i]
    my_list[i]=my_list[j]
    my_list[j]=temp
    i+=1
    j-=1

print(f"The reversed list is {my_list}")
#The following is using reverse()
# my_list.reverse()
# print(my_list)
