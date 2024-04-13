#5) Elaborar um programa Python para verificar se um número é par ou ímpar.

def verifica_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "ímpar"
    
print(verifica_par_impar(44))
