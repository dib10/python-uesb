##6) Elaborar um programa Python para calcular as raízes da equação do segundo grau.
import math

def calcula_raiz(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0: #delta negativo
        return "Não há raízes reais"
    elif delta == 0: #delta igual a zero, raiz única
        return -b/(2*a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    
print(calcula_raiz(1,2,1))
