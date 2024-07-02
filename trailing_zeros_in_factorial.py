#finding the no.of zeros in a factorial of a number
number=eval(input("Enter the non-negative number:"))
count=0
i=5

while (number//i)>0:
    count+=number//i
    i*=5

print(f"The trailing zeros of {number}!={count}")