#Creare unei clase - comentariu
class Student:
    ## "__" -> dunder 
    ## self -> obiectul curent
    def __init__(self, varsta, nume, casatorit=False):
        self.varsta = varsta
        self.nume = nume
        self.este_casatorit = casatorit

    ## "__" -> functii magice
    ## Functia de conversie a obiectului la un string
    def __str__(self):
        return f"Studentul {self.nume} are varsta {self.varsta} ani si { "" if self.este_casatorit else "nu"} este casatorit"
        

#Crearea unor instante (un obiect de tipul Student):
obiect1 = Student(varsta = 22, nume="Ionut")
print(obiect1)

obiect2 = Student(varsta = 30, nume="Andreea")
print(obiect2)

obiect3 = Student(varsta = 40, nume="Florin", casatorit=True)
print(obiect3)