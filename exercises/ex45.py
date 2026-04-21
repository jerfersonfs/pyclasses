mensalidade = float(input("Qual o valor da pago na sua mensalidade hoje? "))

print("Escolha uma forma de pagamento:\n-PIX\n-CARTÃO \n-DINHEIRO")
metodo = str(input("Como deseja pagar? ").lower())

taxa = 0
desconto = 0
valorFinal = 0

if metodo == "cartão":
    print("Essa opção não possui desconto")
elif metodo == "pix":
    taxa = 6 / 100
    desconto = mensalidade * taxa
    valorFinal = mensalidade - desconto
    print(f"De acordo com o metodo de pagamento, o valor fica: R${valorFinal}")
elif metodo == "dinheiro":
    taxa = 10 / 100
    desconto = mensalidade * taxa
    valorFinal = mensalidade - desconto
    print(f"De acordo com o metodo de pagamento, o valor fica: R${valorFinal}")
else:
    print("Opção inválida")

