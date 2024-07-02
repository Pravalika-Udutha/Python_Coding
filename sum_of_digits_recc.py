#finding the sum of digits using recursion

def sum_of_digits(number):
    sum=0
    while number>0:
        temp=number%10
        sum+=temp
        number//=10
    return sum


number=int(input("Enter the number:"))
print(f"The sum of digits of {number} is {sum_of_digits(number)}")