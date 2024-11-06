import random

# Função para mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(spot == jogador for spot in linha):
            return True
    for col in range(3):
        if all(tabuleiro[row][col] == jogador for row in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    return all(spot != " " for row in tabuleiro for spot in row)

# Função para a jogada do usuário
def jogada_usuario(tabuleiro):
    while True:
        try:
            posicao = int(input("Escolha sua posição (1-9): ")) - 1
            linha, coluna = divmod(posicao, 3)
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X"
                break
            else:
                print("Posição já ocupada. Escolha outra.")
        except (ValueError, IndexError):
            print("Posição inválida. Escolha entre 1 e 9.")

# Função para a jogada do programa
def jogada_programa(tabuleiro):
    posicoes_livres = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == " "]
    if posicoes_livres:
        linha, coluna = random.choice(posicoes_livres)
        tabuleiro[linha][coluna] = "0"

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    mostrar_tabuleiro(tabuleiro)
    
    while True:
        jogada_usuario(tabuleiro)
        mostrar_tabuleiro(tabuleiro)
        if verificar_vencedor(tabuleiro, "X"):
            print("Parabéns! Você venceu!")
            break
        if tabuleiro_cheio(tabuleiro):
            print("O jogo terminou em empate!")
            break
        
        jogada_programa(tabuleiro)
        mostrar_tabuleiro(tabuleiro)
        if verificar_vencedor(tabuleiro, "0"):
            print("O programa venceu! Tente novamente.")
            break
        if tabuleiro_cheio(tabuleiro):
            print("O jogo terminou em empate!")
            break

# Iniciar o jogo
jogo_da_velha()

    