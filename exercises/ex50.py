nome = str(input("Digite seu nome: "))
notas = []
total = 0

for i in range(3):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)
    total += nota

media = total / 3

if media > 7:
    print(f"{nome}! Sua média foi de {media} e você foi aprovado")
elif media < 7 and media > 5:
    print(f"{nome}! Sua média foi de {media} e você está de recuperação")
elif media < 5:
    print(f"{nome}! Sua média foi de {media} e você foi reprovado")
else:
    print(f"Resultado inesperado")