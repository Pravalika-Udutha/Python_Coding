#finding the given year is leap year or not
year=eval(input("Enter the Year:"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")