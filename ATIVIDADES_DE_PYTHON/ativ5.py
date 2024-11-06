#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário 
# e imprima a data com o nome do mês por extenso.

# Dicionário para converter números de mês em nomes por extenso
meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março",
    "04": "abril", "05": "maio", "06": "junho",
    "07": "julho", "08": "agosto", "09": "setembro",
    "10": "outubro", "11": "novembro", "12": "dezembro"
}

# Solicita a data de nascimento
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Separa o dia, mês e ano
dia, mes, ano = data.split("/")

# Converte o mês para o nome por extenso
mes_extenso = meses.get(mes, "Mês inválido")

# Imprime a data com o mês por extenso
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")


