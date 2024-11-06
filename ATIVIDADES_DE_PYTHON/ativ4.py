#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Exibe o nome em formato de escada invertida
for i in range(len(nome)):
    print(" " * i + nome[i:].upper())

