#17) Elaborar uma função para dobrar os elementos de uma lista.

lista = [1,2,3,4,5,6,7,8,9,10]
def dobra_lista(lista):
    return [x*2 for x in lista]

print(dobra_lista(lista))
