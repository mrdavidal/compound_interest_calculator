years = input("Enter the number of years:")
anual_interest_rate = input("Enter the anual interest rate:")
monthly_deposit = input("Monthly deposit:")
try:
    years = int(years)
    anual_interest_rate = float(anual_interest_rate)
    monthly_deposit = float(monthly_deposit)
except:
    print("Something went wrong, please try again!")
# compound interest if interest is composed monthly (percentage of the anual interest rate gets composed monthly)
def compound_interest_monthly(y , r, d):
    months = y * 12
    monthly_rate = r / 12
    sum = 0
    rate = 0
    while months > 0:
        sum = sum + rate + d
        rate = (sum * monthly_rate) / 100
        months -= 1
    return round(sum, 2)
# compound interest if interest is composed yearly
def compound_interest_yearly(y, r, d):
    years = y
    yearly_deposit = d * 12
    sum = yearly_deposit
    rate = 0
    while years > 0:
        if years == y:
            sum = sum + rate
        else:
            sum = sum + rate + yearly_deposit
        rate = (sum * r) / 100
        years -= 1
    sum += rate
    return round(sum, 2)
# compound interest if interest is composed daily
start_year = input("Enter the year to start the calculation from:")
"""
start_month = input("Enter the month to start the calculation from:")
start_day = input("Enter the day you want to start the calculation from:")
"""
try:
    start_year = int(start_year)
except:
    print("You haven't entered a year!")

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_year(start_y, years_on):
    total_years = start_y + years_on
    days = []
    while start_y <= total_years:
        if is_year_leap(start_y):
            days.append(366)
        else:
            days.append(365)
        start_y += 1
    return days

def days_in_month(year, month):
    leap_year = [31,29,31,30,31,30,31,31,30,31,30, 31]
    common_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        return leap_year[month - 1]
    else:
        return common_year[month - 1]
    return None

def compound_interest_daily(start_year, y, r, d):
    days_over_years = days_in_year(start_year, y)
    daily_rate = []
    for nr in days_over_years:
        daily_rate.append(r/nr)
    month = 1

print("If compund interest is composed mothly",compound_interest_monthly(years, anual_interest_rate, monthly_deposit))
print("If compund interest is composed anually",compound_interest_yearly(years, anual_interest_rate, monthly_deposit))
print(compound_interest_daily(start_year, years, anual_interest_rate, monthly_deposit))
