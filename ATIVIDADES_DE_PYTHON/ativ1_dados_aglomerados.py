# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para ler 5 números inteiros do usuário
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Exibe os números inseridos
print("\nOs números digitados foram:")
for numero in numeros:
    print(numero)
