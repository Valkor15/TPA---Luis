#Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem 
#diferente para cada um dos casos a seguir:
#A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”; 
#B) Se a média for menor que 7 e maior que 5, exiba a mensagem “Você ficou com média 
#(media) e está de recuperação; 
#C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”

nome = str(input('Digite o nome do aluno: '))
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segundo nota: '))
num3 =  float(input('Digite a terceiro nota: '))

media = (num1 + num2 + num3) / 3

if media > 7:
    print ('Você tirou {}, Parabéns {} você passou'.format (media, nome))

if media <= 7 and media >= 5:
    print ('Você tirou {}, {} você ficou com a média'.format (media, nome))

if media < 5:
    print ('Você tirou {}, ESTÁ REPROVADO'.format (media))