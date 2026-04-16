# Algoritmo para calcular notas
nome = str(input("Escreva seu nome"))

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite outra nota: "))

media = (n1+n2)/2

if media >= 7:
    print(f"Parabens {nome} você foi aprovado!")
elif media >=5 & media <7:
    print(f"{nome} você está de recuperação")
elif media <5:
    print("Você foi reprovado")
else:
    print("Opção nula")
