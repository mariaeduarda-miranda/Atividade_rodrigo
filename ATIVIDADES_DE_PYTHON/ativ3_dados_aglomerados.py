# Faça um programa que preencha um vetor de dez números e encontre o maior elemento.

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para ler 10 números inteiros do usuário
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Encontra o maior número na lista
maior_numero = max(numeros)

# Exibe o maior número
print(f"\nO maior número digitado é: {maior_numero}")