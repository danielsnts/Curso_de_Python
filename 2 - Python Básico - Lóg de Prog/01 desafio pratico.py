ano_atual = int(2022)
nome = str(input("Nome: "))
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

print(f"Nome: {nome}",
      f"Ano de Nascimento: {ano_atual-idade}",
      f"IMC : {peso/(altura**2)}")
