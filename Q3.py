year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("The year is not a leap year")
elif year % 4 == 0 or year % 400 == 0:
    print("The year is a leap year")
