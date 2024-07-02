#printing the no.of digits in a number that can divide it

#user input
num=eval(input("Enter the Number:"))
count=0
rep_num=num
while num>0:
    #for getting last digit of every number
    temp=num%10
    #checking for divisiblity
    x=rep_num%temp
    if x==0:
        count+=1
    num//=10

print(f"The no.of digits in a number that can divide it is {count}")