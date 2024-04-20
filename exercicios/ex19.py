#19) Elaborar uma função recursiva em Python para calcular o MDC de dois números.


def calcular_mdc(a,b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a%b)
    
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
mdc = calcular_mdc(a,b)
print(f"O MDC de {a} e {b} é: {mdc}")