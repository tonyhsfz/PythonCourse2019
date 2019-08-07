
class Clock:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    ## Print the Clock
    def __str__(self):
        if self.minutes < 10:
            return 'It is %d:0%d now.' % (self.hour, self.minutes)
        else: return 'It is %d:%d now.' % (self.hour, self.minutes)

    ## Add the time
    def __add__(self, minutes):
        self.minutes += minutes
        extra_hour = self.minutes//60
        remaining_minutes = self.minutes%60
        self.minutes = remaining_minutes
        self.hour += extra_hour
        self.hour = self.hour%24
        if self.minutes < 10:
            return 'It is %d:0%d after the addition.' % (self.hour, self.minutes)
        else: return 'It is %d:%d after the addition.' % (self.hour, self.minutes)


    ## Subtract time
    def __sub__(self, minutes):
        sub_hour = minutes//60
        sub_minutes = minutes%60
        self.minutes -= sub_minutes
        if self.minutes < 0:
                self.minutes += 60
                self.hour -= 1
        self.hour -= sub_hour
        while self.hour < 0:
                self.hour += 24
        if self.minutes < 10:
            return 'It is %d:0%d after the subtraction.' % (self.hour, self.minutes)
        else: return 'It is %d:%d after the subtraction.' % (self.hour, self.minutes)

    ## Are two times equal?
    def __eq__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return "True"
        else: return "False"

    ## Are two times not equal?
    def __ne__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return "False"
        else: return "True"

clock1 = Clock(10, 5)
print(clock1)
print(clock1+61)
print(clock1+61)
print(clock1+9000)

clock2 = Clock(10, 5)
print(clock2)
print(clock2-5)
print(clock2-61)
print(clock2-9000)

clock1 = Clock(10, 5)
clock2 = Clock(10, 5)
print(clock1 == clock2)
print(clock1 != clock2)
print(clock1 == Clock(10, 5))
print(clock2 != Clock(0, 23))
