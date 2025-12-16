"""Definiți clasa Motor conținând informații despre seria motorului, puterea acestuia și numărul de kilometri parcurși. Aceste atribute trebuie sa fie private și să existe proprietăți (decorator)"""


class Motor:

    def __init__(self, serie, putere, km=0):
        self.__serie = serie
        self.__putere = putere
        self.__km = km

    def __str__(self):
        return f"Motorul cu seria {self.serie} are {self.putere} CP"
    
    @property
    def serie(self):
        return self.__serie

    @property
    def km_parcursi(self):
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

    print("Puterea motorului", m1.putere)
    m1.putere = 312
    print("Puterea motorului", m1.putere)
