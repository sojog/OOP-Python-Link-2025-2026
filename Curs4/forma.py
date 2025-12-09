

### DEFINIRE
class Rectangle:
    """Clasa Rectangle abstractizează un dreptunghi dintr-un plan (lungime și lățime).
        Clasa deţine următoarele caracteristici:
            Lungimea și lățimea dreptunghiului.
        Clasa deţine următoarele implementări:
            show - se printează dimensiunile dreptunghiului;
            resize - se modifică lungimea și lățimea;
            set_to_square - se setează lungimea egală cu lățimea pentru a forma un pătrat;
            area - calculează aria dreptunghiului.
            is_square - spune dacă un dreptunghi este pătrat"""
    def __init__(self, lungime = 0, latime = 0):
        self.lungime = lungime
        self.latime = latime 
    def __str__(self):
        return f"{self.lungime} x {self.latime}"
    
    def show(self):
        print(self)

    def resize(self, lungime_noua, latime_noua):
        self.lungime = lungime_noua
        self.latime = latime_noua 

    def set_to_square(self):
        self.lungime = self.latime

    @property
    def area(self):
        return self.lungime * self.latime

    def is_square(self):
        return self.lungime == self.latime
