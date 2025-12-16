"""Suprascrieți funcție de transformare a motorului la int care întoarce numărul de km parcurși
Suprascrieți operatorul += pentru a adăuga km la km parcurși"""

class Motor:
    def __init__(self, serie, putere, km=0):
        self.__serie = serie
        self.__putere = putere
        self.__km = km

    def __str__(self):
        return f"Motorul cu seria {self.serie} are {self.putere} CP si {self.kilometraj} km parcursi"
    
    def __int__(self):
        return self.kilometraj
    
    def __add__(self, distance):
        if type(distance) == int and distance >= 0:
            self.__km += distance

        return self
    
    @property
    def serie(self):
        return self.__serie

    @property
    def kilometraj(self):
        return self.__km

    @property
    def putere(self):
        return self.__putere
    
    @putere.setter
    def putere(self, new_value):
        if type(new_value) == int and new_value > 0:
            self.__putere = new_value



if __name__ == "__main__":
    m1 = Motor("31241", 100, 4)
    print(m1)

    m1 += 100
    print(m1)
    
    m1 += 123