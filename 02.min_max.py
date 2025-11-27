
# lista = []
# if not lista:
#     print("Adevarat")
# else:
#     print("Fals")



def min_max(lista):
    if not lista:
        return "Lista este goala"
    
    minim, maxim = lista[0], lista[0]

    for i in lista:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i

    return minim, maxim

l = [ 42 , 13 , 61 , 2 , -42, 868 , 1, -11 , -32, 300]
print(min_max(l))

print(min_max([]))

