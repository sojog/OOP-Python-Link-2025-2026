
class TimeConverter:

    def __init__(self, hours = 0, minutes = 0):
        self.__total_minutes = hours * 60 + minutes

    def __str__(self):
        return f"{self.minutes // 60}h:{self.minutes % 60}m"

    ## Conversie la int    
    def __int__(self):
        return self.minutes

    ## t1 == t2
    ## self == value
    def __eq__(self, value):
        return self.minutes == value.minutes
    
    ## Operator overload

    ## t1 += 10
    ## t1 = t1 + 10
    def __iadd__(self, value:int):
        self.__total_minutes += value
        return self 
    
    ## t1 -= 10
    ## t1 = t1 - 10
    def __isub__(self, value:int):
        self.__total_minutes -= value
        return self 

    ## t1 + t2
    def __add__(self, value:TimeConverter):
        return self.minutes + value.minutes
    
    ## t2 - t1
    def __sub__(self, value:TimeConverter):
        return self.minutes - value.minutes

    @property
    def minutes(self):
        return self.__total_minutes

    ## t1 += 10

t1 = TimeConverter(2, 30)
t2 = TimeConverter(2, 30)

print(t2.minutes)
print(t2)


print(str(t1)) ## Merge oricum. Daca e implementat __str__ atunci returneaza acea valoare
print(int(t1)) ## Merge doar daca ma implementata functia __int__

print(t2 == t1) ## De comparat valorile
t3 = t1
print(t1 == t3)

print("Adresa lui t1:", id(t1))
print("Adresa lui t2:", id(t2))
print("Adresa lui t3:", id(t3))


# print(t2 - t1) ## Nu merge

 
print(t1)
t1 += 10 ## Nu merge, dar as putea sa o implementez
print(t1)


t1 += 100 ## Nu merge, dar as putea sa o implementez
print(t1)

t1 -= 120
print(t1)


print(TimeConverter(2,30) - TimeConverter(1,59))