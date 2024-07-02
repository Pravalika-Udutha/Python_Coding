#counting the number of digits in a number

num=eval(input("Enter the number:"))
count=0
replicated_num=num
#zeros case
if num==0:
    count=1
    print("Irrespective of number of zeros provided,")
#non zeros positive case
else:
    num=abs(num) #for making all the positive and negative integers into positive integers 
    #now it works for all integers except zero
    while num>0:
        num=num//10
        count+=1

print(f"The {replicated_num} has {count} digits in it!!!")