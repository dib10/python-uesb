#9) Elaborar um programa Python para imprimir a tabuada de um numero. 

def tabuada(n):
    for i in range(0,11): #isso pq range nao engloba o ultimo numero
        print(f"{n} x {i} = {n*i}")
n = int(input("Digite o número: "))
tabuada(n)
