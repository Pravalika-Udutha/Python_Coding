number=int(input("Enter the number:"))

#consider a list that has all vales with true
prime=[True for i in range(number+1)]
p=2
while p*p<=number:
    if prime[p]==True:
        for i in range(p*p,number+1,p):
            prime[i]=False
    p+=1
for i in range(2,number+1):
    if prime[i]==True:
        print(i)