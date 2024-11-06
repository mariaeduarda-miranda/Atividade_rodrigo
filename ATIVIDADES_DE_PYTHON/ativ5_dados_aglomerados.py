#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
#organizações

#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
#mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
#Não deverão seraceitos valores além dos válidos para o programa (0 a 6). 
#Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
#Após os dados terem sido completamente informados, 
#o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
#O formato da saída foi dado pela empresa, e é o seguinte

# Opções de sistemas operacionais
sistemas = [
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro"
]

# Vetor para armazenar os votos de cada sistema operacional
votos = [0] * len(sistemas)

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
for i, sistema in enumerate(sistemas, start=1):
    print(f"{i} - {sistema}")
print("Digite 0 para encerrar a votação.")

# Leitura dos votos
while True:
    voto = input("Informe o número do sistema operacional (1-6) ou 0 para encerrar: ")

    if voto.isdigit():
        voto = int(voto)
        if voto == 0:
            break
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1
        else:
            print("Opção inválida! Digite um número entre 1 e 6.")
    else:
        print("Entrada inválida! Digite um número inteiro entre 1 e 6.")

# Cálculo do total de votos
total_votos = sum(votos)

# Exibição dos resultados
print("\nSistema Operacional    Votos   %")
print("-" * 32)
for i, sistema in enumerate(sistemas):
    percentual = (votos[i] / total_votos * 100) if total_votos > 0 else 0
    print(f"{sistema:<20} {votos[i]:<8} {percentual:.2f}%")

# Determinação do vencedor
vencedor_index = votos.index(max(votos))
vencedor = sistemas[vencedor_index]
votos_vencedor = votos[vencedor_index]
percentual_vencedor = (votos_vencedor / total_votos * 100) if total_votos > 0 else 0

print("\n------------------------------------")
print(f"O Sistema Operacional mais votado foi o {vencedor}, com {votos_vencedor} votos, correspondendo a {percentual_vencedor:.2f}% dos votos.")