"""Trebuie creată clasa Point care sa abstractizeze un punct dintr-un plan (coordonate x si y)
Clasa deţine următoarele caracteristici:
Punctul x si punctul y
Clasa deţine următoarele implementari:
show - se printeaza coordinatele punctului;
move - se muta coordonatele;
setToOrigin - se seteaza coordinatele (0, 0);
dist - distanta intre doua puncte"""

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __sub__(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def show(self):
        print(self)
    
    def dist(self, other):
        print(self - other)

    def move(self, new_x, new_y):
        if type(new_x) == int and type(new_y) == int:
            self.__x = new_x
            self.__y = new_y

    def set_to_origin(self):
        self.move(0, 0)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    


p1 = Point(1, 1)
p2 = Point(3, 4)

print("p1:", p1)
p1.set_to_origin()
print("p1:", p1)

print(p2 - p1)
p2.dist(p1)