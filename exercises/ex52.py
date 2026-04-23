valorProd = float(input("Digite o valor de um produto: "))
taxaSete = 7 / 100
juros = valorProd * taxaSete
valoFim = valorProd + juros

parcelas = valoFim / 10
print(f"Com parcelas de 10x, vai ser pago R${parcelas} p/ mês")