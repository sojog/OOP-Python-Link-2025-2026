
class Angajatul:
    def __init__(self, nume, salariu_lunar):
        self.nume = nume
        self.salariu_lunar = salariu_lunar
    def salariu_anual(self):
        return self.salariu_lunar * 12

    def increase_salary(self, procent):
        self.salariu_lunar += self.salariu_lunar * procent / 100

    def compare_salary(self, other):
        if self.salariu_anual > other.salariu_anual:
            return f"{self.nume} are un salariu anual mai mare decat {other.nume}."
        elif self.salariu_anual < other.salariu_anual:
            return f"{other.nume} are un salariu anual mai mare decat {self.nume}."
        else:
            return f"{self.nume} si {other.nume} au acelasi salariu anual."
    
    def __str__(self):
        return f"Angajatul {self.nume} are salariul de {self.salariu_anual()} pe an."

angajat1 = Angajatul("Alex", 3000)
angajat2 = Angajatul("Maria", 3500)

operation = input("Ce operatie doresti sa efectuezi? (compare/increase/display): ")

# Increase
if operation == "increase":
    angajatulales1 = input("Introdu numele angajatului caruia doresti sa ii maresti salariul: ")
    if angajatulales1 == "Alex":
        procent = float(input("Introdu procentul de marire a salariului: "))
        angajat1.increase_salary(procent)
        print(f"Salariul lunar al lui {angajat1.nume} dupa marire este: {angajat1.salariu_lunar}")
    elif angajatulales1 == "Maria":
        procent = float(input("Introdu procentul de marire a salariului: "))
        angajat2.increase_salary(procent)
        print(f"Salariul lunar al lui {angajat2.nume} dupa marire este: {angajat2.salariu_lunar}")

# Compare
elif operation == "compare":
    print(angajat1.compare_salary(angajat2))

# Display
elif operation == "display":
    angajatulales2 = input("Introdu numele angajatului pe care doresti sa il afisezi: ")
    if angajatulales2 == "Alex":
        print(angajat1)
    elif angajatulales2 == "Maria":
        print(angajat2)
print(angajat1)