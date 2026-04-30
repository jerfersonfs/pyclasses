termo = int(input("Digite o primeiro termo: "))
qtdeTermo = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

print("o PA é:")
print("a 1 ...", termo)

for i in range(0,qtdeTermo):
    termo += razao
    anterior = termo - razao
    print(f"a {anterior} ... {termo}")