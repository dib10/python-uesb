#2) Elaborar um programa Python para somar os digitos de um número menor que 100.

def soma_digitos(num):
    if num <100:
        str_num = str(num)
        soma = 0
        print(str_num)
        for i in str_num:
            soma +=int(i) 
        return soma
    else:
        return 'Número maior que 100'
    
print(soma_digitos(93))
