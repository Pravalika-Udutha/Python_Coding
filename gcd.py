#finding the gcd or hcf of a number

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
gcd=1
#finding the min of numm1 and num2
minimum=min(num1,num2)
#finding gcd
for i in range(1,minimum+1):
    if num1%i==0 and num2%i==0:
        gcd=i

print(f"GCD or HCF of {num1,num2} is {gcd}")