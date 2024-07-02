#finding the factorial of a number using recursion

def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)


number=int(input("enter the number:"))
print(f"The factorial of {number} is {factorial(number)}")