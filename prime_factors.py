#program for checking the prime factors of a number
number = int(input("Enter the number: "))

for i in range(2, number + 1):
    if number % i == 0:  # Check if i is a factor of the number
        is_prime = True
        
        # Check if i is a prime number
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"Prime Factor: {i}")

