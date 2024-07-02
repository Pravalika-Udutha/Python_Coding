number=int(input("Enter the number:"))
if number<=0:
    print("Enter the valid number")
print(f"The divisors of {number} are:")
for i in range(1,number+1):
    if number%i==0:
        print(i)