my_list=[eval(x) for x in input("enter the numbers:").split()]
count=0
for i in my_list:
    if i%2!=0:
        count+=1
        x=i

if count==1:
    print(f"The only odd number in list is {x}")
elif count>1:
    print("The are multiple odd numbers in list")
else:
    print("There is no odd numbers in list i.e., there is all even numbers")
