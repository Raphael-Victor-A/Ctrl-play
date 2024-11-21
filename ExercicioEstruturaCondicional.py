# lados1 = float(input("Digite o primeiro lado: "))
# lados2 = float(input("Digite o segundo lado: "))
# lados3 = float(input("Digite o terceiro lado: "))

# if lados1 == lados2 == lados3:
#     print("Triangulo equilatero")
# elif lados1 == lados2 or lados1 == lados3 or lados2 == lados3:
#     print("Triangulo isosceles")
# else:
#     print("Triangulo escaleno")


# idade = int(input("Digite sua idade: "))

# if idade <= 12:
#     print("Criança ")
# elif idade <= 17:
#     print("Adolescente")
# elif idade <= 60:
#     print("adulto")
# elif idade< 0 or idade > 120:
#     print("Invalida")
# else:
#     print("idoso")

# peso = float(input("Digite o seu peso (kg)"))
# altura = float(input("Digite seu peso em (m)"))

# imc = peso / (altura ** 2)

# if imc < 18.5:
#     print( "Abaixo do peso")
# elif 18.6 < imc < 24.9:
#     print("Peso ideal")
# elif 25 <imc < 29.9:
#     print("acima do peso")
# elif 30 < imc< 39.9:
#     print("obesidade 1")
# else:
#     print("obesidade 2")

nota1 = float(input(" "))
nota2 = float(input(" "))
nota3 = float(input(" "))
nota4 = float(input(" "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 3:
    print("Reprovado")
elif media >= 7:
    print("Aprovado")
else:
    print("exame")

