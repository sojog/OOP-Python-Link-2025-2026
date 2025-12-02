
def render_producedural(width, height):
    print("#" * width)
    for i in range(height-2):
        print("#" + " " * (width - 2) + "#")
    print("#" * width)

render_producedural(10, 10)

## numele clasei cu litera mare:
class Printer:
    
    ## metoda (trebuie sa aibe acel self, daca nu, nu functioneaza)
    def render(self, width, height):
        print("#" * width)
        for i in range(height-2):
            print("#" + " " * (width - 2) + "#")
        print("#" * width)


## Un obiect (instanta)
obiect = Printer()
obiect.render(10, 10)
obiect.render(20, 30)

