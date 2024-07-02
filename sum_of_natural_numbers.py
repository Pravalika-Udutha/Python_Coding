#finding the sum of natural numbers using recursion

#defining the function
def natural_sum(n):
    if n==0:
        return 0
    else:
        return n+natural_sum(n-1)


n=int(input("enter the n value:"))
sum=natural_sum(n)
print(f"The sum of first {n} natural numbers is {sum}")