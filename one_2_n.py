#printing the values from 1 to n and n to 1 using recursion

#from 1 to n
def straight_recursion(n):
    if n>0:
        straight_recursion(n-1)
        print(n,end=" ")
        

def reverse_recursion(n):
    if n>0:
        print(n,end=" ")
        reverse_recursion(n-1)
        

n=int(input("Enter the n value:"))
straight_recursion(n)
print()
reverse_recursion(n)