# Faça um programa que preencha um vetor de dez números inteiros, some todos e exiba o resultado.

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para ler 10 números inteiros do usuário
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Calcula a soma dos números no vetor
soma = sum(numeros)

# Exibe a soma total
print(f"\nA soma dos números digitados é: {soma}")
