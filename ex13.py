#13) Elaborar um programa Python para calcular a soma de 1 ate 50

def calcula_soma():
    soma = 0 
    for i in range(1,51):
        soma+= i
    print(f'A soma de 1 até 50 é: {soma}')


calcula_soma()


