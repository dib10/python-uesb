#18) Elaborar uma função em Python para computar o maior e o menor elemento de uma lista.
lista = [1,2,3,4,5,6,7,8,9,3]
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if i> maior:
            maior = i
        elif i< menor:
            menor = i
    return maior, menor
    
print(maior_menor(lista))