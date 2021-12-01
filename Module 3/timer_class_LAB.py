# constructor should accept three arguments: hours in [0..23], minutes [0..59], seconds [0..59]
# default values should be zero
# objects should be printable - they should implicitly convert themselves to strings of the form "hh:mm:ss" with leading zeros when required
# class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored by +1/-1 second respectively
# object properties should be private

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self): 
        if self.__hours < 10:
            hour_str = "0" + str(self.__hours)
        else:
            hour_str = str(self.__hours)
        
        if self.__minutes < 10:
            min_str = "0" + str(self.__minutes)
        else:
            min_str = str(self.__minutes)
        
        if self.__seconds < 10:
            sec_str = "0" + str(self.__seconds)
        else:
            sec_str = str(self.__seconds)
                            
        return hour_str + ":" + min_str + ":" + sec_str

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else: 
                    self.__hours += 1
            else: 
                self.__minutes += 1
        else: 
            self.__seconds += 1

    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hours == 0:
                    self.__hours = 23
                else:
                    self.__hours -= 1
            else: 
                self.__minutes -= 1
        else: 
            self.__seconds -= 1
        


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
