
## numele clasei cu litera mare:
class Printer:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    ## metoda (trebuie sa aibe acel self, daca nu, nu functioneaza)
    def render(self):
        print("#" * self.width)
        for i in range(self.height-2):
            print("#" + " " * (self.width - 2) + "#")
        print("#" * self.width)


## Un obiect (instanta)
obiect = Printer(10, 20)
obiect.render()


obiect2= Printer(3, 3)
obiect2.render()