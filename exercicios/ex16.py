#16) Elaborar uma função para calcular o maior de três números.

import math
nums = []
def maior_de_tres(a,b,c):
    nums.append(a)
    nums.append(b)
    nums.append(c)
    return max(nums)    


a = float(input("Digite o primero número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
maior = maior_de_tres(a,b,c)
print(f"O maior número é: {maior}")