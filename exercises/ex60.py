# 60 - Escreva um algoritmo que solicite números que devem ser inseridor em uma lista e em seguida ser ordenado de maneira
# crescente antes de ser exíbido para o usuário. O programa deve ser encerrado quando usuário entrar com valor zero

times = int(input("Quantas vezes você quer que esse programa rode? "))
if times == 0:
    print("Progama encerrado")
numeros = []
for i in range(0,times):
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Programa encerrado")
        break
    else:
        numeros.append(numero)
if times > 0:
    print("Números em ordem: ")
    numeros.sort()

for num in numeros:
    print(num)

## solução

# numeros = [0]
# while True
# num = int(input("Entre com um número: "))
# if num != 0:
# numeros.append(num)
# numeros.sort()
# tamanho = len(numeros)
# print("Lista atualizada")
# for i in range(tamanho):
# print(numeros[i])
#else
#break
# programa encerrado