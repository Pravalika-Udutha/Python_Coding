#program for checking a given number is palindrome or not 

#reading the user input
number=eval(input("Enter the Number:"))

#in order not to loss the original value store it in other var
oth_var=number

#case 1:if number is zero then it is a palindrome
if number==0:
    print(f"The {number} is a palindrome number")
#case 2:if a number is negative then it is not a palindrome 
#example: -121=121- which is not a plaindrome
elif number<0:
    print(f"The {number} is not a palindrome number")

#case 3:if a number is non-zero positive integer then we have to check for palindrome
else:
    rev_num=0
    while number>0:
        temp=number%10
        rev_num=rev_num*10+temp
        number//=10
    if rev_num==oth_var:
        print(f"The {oth_var} is a palindrome number")
    else:
        print(f"The {oth_var} is not a palindrome number")
