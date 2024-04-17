#11) Elaborar um programa Python para verificar se uma string é uma palindrome. 


def verifica_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == inverter:
        return 'Palíndromo'
    else:
        return 'Não é Palíndromo'
    
palavra = input('Digite uma palavra: ')
inverter = palavra[::-1]
print(f'{verifica_palindromo(palavra)}, {inverter}')

