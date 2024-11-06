#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Exibe o nome em formato de escada invertida
for i in range(len(nome), 0, -1):
    print(nome[:i].upper())
