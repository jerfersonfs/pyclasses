# Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago

p1 = float(input("Digite o preço de um produto:"))
p2 = float(input("Digite o preço de outro produto:"))

d1 = 8 / 100
r1 = p1 - d1
d2 = 11 / 100
r2 = p2 - d2

print(f"Com os descontos o valor 1° produto é: {r1} e do 2° é: {r2}")
