# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# lista_notas = [nota1, nota2, nota3, nota4]

# media = sum(lista_notas) / len(lista_notas)

# print(f"A media das notas é: {media}")

nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite seu peso: "))

nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite seu peso: "))

notas = [nota1, nota2]
pesos = [peso1, peso2]

somaPonderado = sum(notas)
somaPesos = sum(pesos)

mediaPonderada = somaPonderado / somaPesos

print(f"A media ponderada das notas é: {mediaPonderada}")