#adding the digits of a number untill it becomes as 1 digit

#user input
num=eval(input("Enter the number:"))
actual=num

while num>9:
    total=0
    while num>0:
        temp=num%10
        total+=temp
        num//=10
    
    num=total
   

print(f"The 1 digit value of {actual} is {num}")

