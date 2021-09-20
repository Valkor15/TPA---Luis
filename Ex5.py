# Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou, por exemplo, 
#o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120

result=1
cont=1

Num = int(input("Digite um número e vamos mostrar quanto que é o fatorial dele: ") )

while cont <= Num:
    result *= cont
    cont += 1

print('resultado do fatorial de {} é {}'.format (Num, result))