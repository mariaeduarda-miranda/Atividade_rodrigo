import time
import random

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 5
        self.felicidade = 5
        self.energia = 5
        self.vivo = True

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Fome: {self.fome}/10")
        print(f"Felicidade: {self.felicidade}/10")
        print(f"Energia: {self.energia}/10\n")

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 2
            print(f"Você alimentou {self.nome}. Fome diminuída!")
        else:
            print(f"{self.nome} já está satisfeito!")
        self._passar_tempo()

    def brincar(self):
        if self.felicidade < 10:
            self.felicidade += 2
            self.energia -= 1
            print(f"Você brincou com {self.nome}. Felicidade aumentada!")
        else:
            print(f"{self.nome} já está muito feliz!")
        self._passar_tempo()

    def dormir(self):
        if self.energia < 10:
            self.energia += 3
            print(f"{self.nome} dormiu e recuperou energia!")
        else:
            print(f"{self.nome} já está cheio de energia!")
        self._passar_tempo()

    def _passar_tempo(self):
        # Conforme o tempo passa, a fome aumenta e a felicidade pode diminuir
        self.fome += random.randint(1, 2)
        self.felicidade -= random.randint(0, 1)
        self.energia -= random.randint(0, 1)

        # Limita os valores entre 0 e 10
        self.fome = min(max(self.fome, 0), 10)
        self.felicidade = min(max(self.felicidade, 0), 10)
        self.energia = min(max(self.energia, 0), 10)

        # Verifica se o bichinho ainda está vivo
        if self.fome >= 10:
            print(f"{self.nome} ficou com muita fome e não resistiu...")
            self.vivo = False
        elif self.felicidade <= 0:
            print(f"{self.nome} ficou muito triste e foi embora...")
            self.vivo = False
        elif self.energia <= 0:
            print(f"{self.nome} está exausto e desmaiou...")
            self.vivo = False

def main():
    print("Bem-vindo ao Tamagotchi!")
    nome = input("Dê um nome ao seu bichinho: ")
    tamagotchi = Tamagotchi(nome)

    while tamagotchi.vivo:
        tamagotchi.mostrar_status()
        print("O que você deseja fazer?")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Dormir")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == "1":
            tamagotchi.alimentar()
        elif escolha == "2":
            tamagotchi.brincar()
        elif escolha == "3":
            tamagotchi.dormir()
        elif escolha == "4":
            print(f"Até logo! {tamagotchi.nome} vai sentir sua falta.")
            break
        else:
            print("Opção inválida! Tente novamente.")

        # Pausa para simular o passar do tempo
        time.sleep(1)

    if not tamagotchi.vivo:
        print(f"{tamagotchi.nome} infelizmente não está mais com você. Fim de jogo.")

if __name__ == "__main__":
    main()