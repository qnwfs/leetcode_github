from datetime import date

def dayOfTheWeek(day: int, month: int, year: int):
    x = date(year, month, day).weekday()
    if x == 0:
        return 'Monday'
    if x == 1:
        return 'Tuesday'
    if x == 2:
        return 'Wednesday'
    if x == 3:
        return 'Thursday'
    if x == 4:
        return 'Friday'
    if x == 5:
        return 'Saturday'
    if x == 6:
        return 'Sunday'

day = 31
month = 8
year = 2019
print(dayOfTheWeek(day,month,year))