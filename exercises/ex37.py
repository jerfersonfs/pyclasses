valor = float(input("Digite o valor de um produto: "))
print(f"R${valor}")

taxa = 10 / 100
precodesc = taxa * valor
precofim = valor - precodesc
print(f"O produto custa R${valor} com a taxa de 10% de desconto (R${precodesc}) ficou: R${precofim}")