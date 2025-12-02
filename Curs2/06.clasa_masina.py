

class Masina:
    def __init__(self, brand, cp):
        self.brand = brand
        self.cai_putere = cp

    def __str__(self):
        return f"Masina {self.brand} are {self.cai_putere} cp"


dacia = Masina("Logan", 70)
print(dacia)

bmw = Masina("Seria3", 170)
print(bmw)