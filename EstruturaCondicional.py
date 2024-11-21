# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Voce é maior de idade")
# else:
#     print("Voce é menor de idade")



# notas = int(input(""))

# if notas >= 10:
#     print("Você passou")
# elif notas >=6:
#     print("Voce esta de recuperação")
# else:
#     print("Exame direto")

idade = int(input("Digite sua idade: "))
temCNH = True

if idade >=18 or temCNH: # ||
    print("Pode dirigir cidadão")
else:
    print("Nao pode dirigir")