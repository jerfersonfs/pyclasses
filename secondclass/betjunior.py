import random

print("--------------------------------------------------")
print("                     BETJunior                    ")
print("--------------------------------------------------")

segredo = random.randrange(1,11)
#print(segredo)

tentativas = 3

for i in range(1,4):
    print("Você possui ",tentativas," tentativas de 3\n")
    numero = int(input("Digite um número entre 1 a 10: "))
    if numero >= 1 and numero <= 10:
        if numero == segredo:
                print("--------------------------------------------------")
                print("              VOCÊ ACERTOU!!! PARABÉNS            ")
                print("--------------------------------------------------")
                break
        else:
                tentativas -=1
                print(f"Você errou! Agora tem {tentativas} tentativas Tente novamente\n")
    else:
        tentativas -=1
        print(f"Número inválido, agora você possui {tentativas}")
print("Fim do jogo")