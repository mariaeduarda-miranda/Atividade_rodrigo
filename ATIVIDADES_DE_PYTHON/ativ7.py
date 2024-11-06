# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

# Inicializa uma lista vazia para armazenar os caracteres
caracteres = []
consoantes = []

# Lista das vogais para referência
vogais = ['a', 'e', 'i', 'o', 'u']

# Lê 10 caracteres do usuário
for i in range(10):
    char = input(f"Digite o caractere {i + 1}: ").lower()
    caracteres.append(char)
    # Verifica se é uma consoante (não é vogal e é uma letra)
    if char.isalpha() and char not in vogais:
        consoantes.append(char)

# Exibe a quantidade de consoantes e quais foram lidas
print(f"Foram lidas {len(consoantes)} consoantes.")
print("As consoantes são:", ' '.join(consoantes))
