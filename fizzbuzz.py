#Important program **asked in may interviews
num=int(input("Enter the natural number:"))

#printing
#case 1: if multiple of 3 then 'fizz'
for number in range(1,num+1):
    if number%3==0 and number%5!=0 :
        print('Fizz')
    #case 2: if multiple of 5 then 'buzz'
    elif number%5==0 and number%3!=0:
        print("Buzz")
    elif number%3==0 and number%5==0:
        print("FizzBuzz")
    else:
        print(number)