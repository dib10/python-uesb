# Elaborar um programa Python para calcular o fatorial de um número.

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1,n):
            n = n * i
        return n
    
print(calcular_fatorial(12))

