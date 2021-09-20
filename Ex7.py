#Escreva um algoritmo que receba dois números e exiba para o usuário todos os valores 
#intermediários a eles, veja exemplo:
#Primeiro número: 5 
#Segundo número: 15 
#Resultado: 6 7 8 9 10 11 12 13 14

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 >= num2:
    while num1 >= num2:
        print (num2)
        num2 += 1
        
if num1 <= num2:
    while num1 <= num2:
        print (num1)
        num1 += 1
        
        