#2. Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome 
#e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Converte o nome para maiúsculas e inverte a ordem das letras
nome_invertido = nome.upper()[::-1]

# Exibe o nome invertido
print(nome_invertido)



