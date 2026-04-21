letra = input("Digite uma letra: ").lower()

vogais = ["a", "e", "i", "o", "u"]

if not letra.isalpha() or len(letra) != 1: # isalpha verifica se é uma letra e len verifica se foi só um caracter
    print("Entrada inválida")
elif letra in vogais:
    print("Vogal")
else:
    print("Consoante")