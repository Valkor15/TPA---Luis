# Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas 
# pessoas são maiores de idade.

nasc= 0
cont = 1
total = 0

while cont <= 10:
    cont += 1
    nasc = int(input('Digite o ano que você nasceu: '))
    MaiorIdade = 2021 - nasc
    if MaiorIdade >= 18:
        total += 1
print ('{} São maiores de idade'.format (total))
