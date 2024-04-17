#4) Elaborar um programa Python para imprimir os divisores de um número

def divisores(num):
    for i in range(1,num+1): #num+1 pq range não inclui o último número
        if num % i == 0:
            print(i)
divisores(60)