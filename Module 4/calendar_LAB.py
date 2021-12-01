import calendar
import datetime as dt

class CalendarPlus(calendar.Calendar):
    def __init__(self):
        calendar.Calendar.__init__(self)

# this just will not work, it returns 61 and 63 for the given samples below, and I have no idea why
#    def count_weekday_in_year(self, year, weekday):
#        count = 0
#        for i in range(1, 13):
#            month = self.monthdays2calendar(year, i)
#            for week in month:
#                for day in week:
#                    if i == 1 and week == month[0]:
#                        if day[0] == 0:
#                            continue
#                        elif day[1] == weekday:
#                            count += 1
#                    elif i == 12 and week == month[-1]:
#                        if day[0] == 0:
#                            continue
#                        elif day[1] == weekday:
#                            count += 1
#                    else:
#                        if day[1] == weekday:
#                            count += 1
#
#        return count


# this one works just fine
    def count_weekday_in_year(self, year, weekday):
        first = dt.date(year, 1, 1).weekday()
        count = 52 # 364 days contains every weekday 52 times
        if (weekday == first + 1) % 7: # if day 365 is the weekday
            count += 1
        if calendar.isleap(year) and (weekday == first + 2) % 7: # if it's a leap year, then if day 366 is the weekday
            count += 1
        return count




cal = CalendarPlus()
print(cal.count_weekday_in_year(2019, 0)) # 52 mondays in 2019
print(cal.count_weekday_in_year(2000, 6)) # 53 sundays in 2000


