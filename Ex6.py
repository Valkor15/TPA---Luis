# Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no 
#primeiro produto, 11% no segundo e apresente o valor final a ser pago.

num1 = int(input('Digite o preço do primeiro produto: '))
num2 = int(input('Digite o preço do segundo Produto: '))

descont1= ((num1 * 8) / 100) - num1
descont2= ((num2 * 11) / 100) - num2
total = (descont1 + descont2) *-1

print ('Com o desconto no primeiro produto de 8% e de 11% no segundo produto, o total vai ser de {}'.format (total))
