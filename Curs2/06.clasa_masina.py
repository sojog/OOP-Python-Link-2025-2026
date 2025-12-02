

class Masina:
    def __init__(self, brand, cp):
        self.brand = brand
        self.cai_putere = cp

    def __str__(self):
        return f"Masina {self.brand} are {self.cai_putere} cp"
    
    ## metoda (functie a clasei)
    def este_puternica(self):
        return self.cai_putere > 100


dacia = Masina("Logan", 70)
print(dacia)
print(dacia.este_puternica())

bmw = Masina("Seria3", 170)
print(bmw)
print(bmw.este_puternica())