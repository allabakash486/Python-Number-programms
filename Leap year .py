year = int(input("Enter the year:"))
def Leap_year(year):
    if (year%400 == 0) or (year%4 == 0 and year %100 != 0):
        return True
    return False
print("Leap Year " if Leap_year(year) else "Not Leap year ")