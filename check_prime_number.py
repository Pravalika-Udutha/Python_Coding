number=int(input("Enter the number:"))
count=2
for i in range(2,number):
    if number%i==0:
        print(f"The number {number} is not a prime number")
        break
    
else:
    print(f"The number {number} is a prime number")