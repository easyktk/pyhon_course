class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    def __init__(self, day):
        if day not in Weeker.__names:
            raise WeekDayError('')
        self.__day = day


    def __str__(self):
        return str(self.__day)

    def add_days(self, n):
        ind = Weeker.__names.index(self.__day)
        ind += n
        self.__day = Weeker.__names[ind % 7]

    def subtract_days(self, n):
        ind = Weeker.__names.index(self.__day)
        ind -= n
        self.__day = Weeker.__names[ind % 7]



try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
