#Classe Bola: Crie uma classe que modele uma bola:

#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


# Cria uma instância da classe Bola
bola = Bola("azul", 30, "couro")

# Mostra a cor atual
print("Cor atual:", bola.mostraCor())

# Troca a cor da bola
bola.trocaCor("vermelho")

# Mostra a nova cor
print("Nova cor:", bola.mostraCor())
