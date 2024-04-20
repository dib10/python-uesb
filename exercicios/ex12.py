#12) Elaborar um programa Python para intercalar duas listas ordenadas. 

def intercala(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
    for i in range(len(lista2)):
        lista3.append(lista2[i])
    lista3.sort()
    return lista3
lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8,10]
print(intercala(lista1,lista2))