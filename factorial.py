#finding the factorial of non-negative numbers

#user input
number=eval(input("Enter the non-negative number:"))

factorial=1
if number==0 and number==1:
    print(f"the value of {number}!=1")
else:
    for i in range(2,number+1):
        factorial*=i
    print(f"the value of {number}!={factorial}")   
