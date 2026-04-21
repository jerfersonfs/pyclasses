acc = 0
for i in range(10):
    numeros = float(input("Digite um número: "))
    acc += numeros
media = acc / 10
print(f"Acumulador: {acc}")
print(f"Média: {media}")