notas = []
total = 0
pesos = [2,3,5]

for i in range(3): # range pega os valores de determinadas vezes que forem repetidas
    nota = int(input("Digite uma nota: "))
    notas.append(nota) # append agrupa os valores em uma array que forem sendo digitados
    total += nota * pesos[i] # soma os valores que forem sendo digitados
print(f"Suas notas: {notas}")
print(f"O total: {total}")
media = total / sum(pesos) 
print(f"Sua média foi de: {media}")