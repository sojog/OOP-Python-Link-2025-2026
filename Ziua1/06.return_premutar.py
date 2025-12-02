
# lista = ["apa", "mancare", "somn", "pastile"]

# for i in lista:
#     if not len(i) > 5:
#         print("Este mai mic ")
#         break
#     else:
#         print("Mai mare")



def filtrare_cuvinte(lista):
    lista = ["apa", "mancare", "somn", "pastile"]
    lista_noua = []
    for i in lista:
        if len(i) > 5:
            lista_noua.append(i)
    return lista_noua



lista = ["apa", "mancare", "somn", "pastile"]
print(filtrare_cuvinte(lista))