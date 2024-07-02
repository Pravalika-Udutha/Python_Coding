#finding the days in a month using function

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def months_in_days(year,month):
    days_list=[31,29,31,30,31,30,31,31,30,31,30,31]
    if leap_year and month==2:
        return 29
    else:
        return days_list[month-1]
year=int(input("Enter a year:"))
month=int(input("Enter the month:"))
days=months_in_days(year,month)
print(f"no.of days in {year} and {month} is {days}")
