# accepts string from ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# objects should be printable
# day stored in object should change with add_days(n) and subtract_days(n)

class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    def __init__(self, day):
        if day.capitalize() not in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"):
            raise WeekDayError
        else:
            self.__weekday = Weeker.__days[day]


    def __str__(self):
        for key in Weeker.__days.keys():
            if Weeker.__days[key] == self.__weekday:
                return key


    def add_days(self, n):
        self.__weekday += n
        self.__weekday %= 7

    def subtract_days(self, n):
        self.__weekday -= n
        self.__weekday %= 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday) # lab said this should be Thu, which is a typo - 15 days after a monday is a tuesday
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
