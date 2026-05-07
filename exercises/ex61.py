lista = [10, 11, 12, 13, 14, 15, 16]

numero = int(input("Digite um número de 10 a 16: "))

if numero in lista:
    indice = lista.index(numero)
    lista[indice] = 7
    
print(lista)