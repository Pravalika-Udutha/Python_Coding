my_list=[int(x) for x in input("Enter the values:").split()]

value=0
for x in my_list:
    count=0
    while x>0:
        temp=x%10
        count+=1
        x//=10
    if count%2==0:
        value+=1

print(value)