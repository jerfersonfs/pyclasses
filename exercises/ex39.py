salaAtual = float(input("Digite seu salário atual: "))
taxa = 0
reajuste = 0
novoSala = 0
if salaAtual < 500:
    taxa = 15 / 100 
    reajuste = salaAtual * taxa
    novoSala = salaAtual + reajuste
    print(f"Com reajuste de 15%, seu salário é de: R${novoSala}")
elif salaAtual >=500 and salaAtual <=1000:
    taxa = 10 / 100
    reajuste = salaAtual * taxa
    novoSala = salaAtual + reajuste
    print(f"Com reajuste de 10%, seu salário é de: R${novoSala}")
elif salaAtual > 1000:
    taxa = 5 / 100
    reajuste = salaAtual * taxa
    novoSala = salaAtual + reajuste
    print(f"Com reajuste de 5%, seu salário é de: R${novoSala}")
else:
    print("Não é possível calcular")