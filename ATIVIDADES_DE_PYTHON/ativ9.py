#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. 
#Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
#sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)  # Cresce 0,5 cm

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

    def __str__(self):
        return (f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso:.2f}kg, Altura: {self.altura:.2f}cm')

# Exemplo de uso
pessoa1 = Pessoa("João", 20, 70, 175)

print(pessoa1)

# Envelhecendo a pessoa
pessoa1.envelhecer()
print("Após envelhecer:")
print(pessoa1)

# Engordando a pessoa
pessoa1.engordar(2)
print("Após engordar 2 kg:")
print(pessoa1)

# Emagrecendo a pessoa
pessoa1.emagrecer(1)
print("Após emagrecer 1 kg:")
print(pessoa1)

# Crescendo a pessoa
pessoa1.crescer(3)
print("Após crescer 3 cm:")
print(pessoa1)
