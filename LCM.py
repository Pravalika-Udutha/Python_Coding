#finding the lcm of 2 numbers
number1=int(input("Enter the number1:"))
number2=int(input("Enter the number2:"))

minimun=min(number1,number2)
gcd=1
for i in range(1,minimun+1):
    if number1%i==0 and number2%i==0:
        gcd=i
lcm=(number1*number2)//gcd
print(f"The LCM of {number1,number2} is {lcm}")