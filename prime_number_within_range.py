#counting the prime numbers within the range
range_num1=int(input("Enter the start range:"))
range_num2=int(input("Enter the end range:"))
count=0
for i in range(range_num1,range_num2):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
        print(f"The {i} is prime number")

    