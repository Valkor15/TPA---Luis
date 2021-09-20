#2. Escreva um algoritmo que receba 10 valores digitados pelo usuário e no final exiba o maior número.

numero = 0
contador = 1
NumMaior = 0

while contador <= 10:
    numero = int(input('Digite um valor: '))
    if NumMaior < numero:
        NumMaior = numero
    contador +=1
    
print (NumMaior)