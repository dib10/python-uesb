#Elaborar um programa Python para ler uma temperatura em Fahrenheint e converter para Celsius.
def fahrenheit_para_celsius(f):
    c = (f-32) * 5/9
    return c

f = float(input("Digite a temperatura em Fahrenheit:"))
c = fahrenheit_para_celsius(f)
print("A temperatura em Celsius é: {:.2f}".format(c))

