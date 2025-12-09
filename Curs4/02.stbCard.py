
# numele clasei cu litera mare
### DEFINIRE A CLASEI
class CardSTB:

    ## VALOARE STATICA -> apartine clasei (ex: TVA)
    valoare_unei_calatorii = 3
    ## VALOARE STATICA -> apartine clasei (ex: TVA)
    contor = 0

    ## detinator, calatorii, credit -> CE ARE CLASA/OBIECTUL (atribute)
    def __init__(self, detinator = "Nenominal", calatorii = 0 , credit = 0):
        self.detinator = detinator
        self.calatorii = calatorii
        self.credit = credit  
        
        CardSTB.contor += 1
        self.numar_card = CardSTB.contor

    def __str__(self):
        return f" Cardul cu nr {self.numar_card} apartine lui {self.detinator} si are {self.credit} credit si {self.calatorii} calatorii "


    def reincarcare_cu_credit(self, valoare_bani):
        self.credit += valoare_bani

    def reincarcare_cu_calatorii(self, nr_calatorii):
        self.calatorii += nr_calatorii

    def calatoreste(self):
        if self.calatorii > 0:
            self.calatorii -= 1
        elif self.credit >= CardSTB.valoare_unei_calatorii:
             self.credit -= CardSTB.valoare_unei_calatorii
        else:
            print("Cardul trebuie reincarcat!!!!!!!!")

### UTILIZARE A CLASEI


print(CardSTB.valoare_unei_calatorii)



card_ionut = CardSTB()
print(card_ionut)

card_ionut_2 = CardSTB("Ionut")
print(card_ionut_2)

card_maria = CardSTB(detinator = "Maria", credit = 10)
print(card_maria)


card_florin = CardSTB(detinator = "Florin", calatorii = 3, credit=5)
print(card_florin)


for i in range(5):
    card_florin.calatoreste()
    print(card_florin)


card_florin.reincarcare_cu_credit(10)
print(card_florin)

card_florin.credit = "infinit"
print(card_florin)

# card_florin.calatoreste()