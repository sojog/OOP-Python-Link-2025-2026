"""1. Creați clasa TimeConverter cu două proprietăți(atribute): 
- hours - numărul de ore (int)- minutes - numărul de minute (int) 
2. Clasa trebuie să conțină următoarele metode publice:- toMinutes() - convertește timpul total în minute- toHours() - convertește timpul total în ore- addTime() - adună încă un interval de timp și returnează rezultatul în minute- diffTime() - calculează diferența față de alt interval de timp și returnează rezultatul în minute """

class TimeConverter:
    
    ## constructor    
    def __init__(self, hours = 0, minutes = 0):
        self.hours = hours
        self.minutes = minutes % 60
        self.hours += minutes // 60

    def __str__(self):
        return f"{self.hours}:{self.minutes}"
    
    def to_minutes(self):
        return self.hours * 60 + self.minutes

    def to_hours(self):
        return self.hours + round(self.minutes / 60, 2)


    def add_time(self, hours=0, minutes=0):
        self.minutes += minutes
        self.hours += (hours + self.minutes // 60)
        self.minutes =  self.minutes % 60
        
        
    def diff_time(self, other_time_converter:TimeConverter):
        return self.to_minutes() - other_time_converter.to_minutes()    

t1 = TimeConverter(2, 30)
print(t1, "->", t1.to_minutes(), "minutes",  " or ", t1.to_hours(), "hours")

t2 = TimeConverter(1, 82)
print(t2, "->", t2.to_minutes(), "minutes",  " or ", t2.to_hours(), "hours")

t2.add_time(1, 59)
print(t2, "->", t2.to_minutes(), "minutes",  " or ", t2.to_hours(), "hours")


print("t2 - t1", t2.diff_time(t1))