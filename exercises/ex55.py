qtdeNotas = int(input("Digite quantas notas você deseja inserir: "))
total = 0

for i in range(qtdeNotas):
    nota = float(input("Digite uma nota: "))
    total += nota
media = total / qtdeNotas
print(f"Média de notas é: {media}")