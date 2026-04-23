salBruto = float(input("Digite seu salário: R$"))
taxaInss = float(input("Digite a taxa de desconto do INSS: "))
taxaIr = float(input("Digite a taxa de desconto do IR: "))

taxa1 = salBruto * (taxaInss /100)
taxa2 = salBruto * (taxaIr/100)
desconto = taxa1 + taxa2
salario = salBruto - desconto
print("Salário líquido: R$",salario)