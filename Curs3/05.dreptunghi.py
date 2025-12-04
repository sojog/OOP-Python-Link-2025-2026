

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

    def area(self):
        return self.lungime * self.latime

    def is_square(self):
        return self.lungime == self.latime


### FOLOSIRE
obj1 = Rectangle(30, 40)
obj_dir =  dir(obj1)
print(type(obj_dir))


function_names = []
for i in obj_dir:
    if not i.startswith("__") and i not in obj1.__dict__:
        function_names.append(i)


print(function_names)
function_names_str = ", ".join(function_names)


while True:
    actiune = input(f"Alege urmatoare actiune {function_names_str}\n")
    if actiune not in function_names:
        continue
    # func = getattr(obj1, actiune)
    # print(func)
    # func()

    if actiune == "show":
        obj1.show()
    elif actiune == "set_to_square":
        obj1.set_to_square()
        obj1.show()
    elif actiune == "area":
        print(obj1.area())
    elif actiune == "is_square":
        print(obj1.is_square())

    elif actiune == "resize":
        lung = int(input("Inserati lungime noua"))
        lat  =  int(input("Inserati latime noua"))
        obj1.resize(lung, lat)
        obj1.show()