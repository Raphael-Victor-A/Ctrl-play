# senha = 0000

# while(senha != 2002):
#     senha = int(input("Digite a senha: "))
#     if senha != 2002:
#         print("Senha invalida!")
# print("ACESSO PERMITIDO")

primeiroNumero = 0
segundoNumero = 1
sequenciaFibonacci = [primeiroNumero, segundoNumero]

for indice in range(2,46):
    proximoNumero = primeiroNumero + segundoNumero
    primeiroNumero = segundoNumero
    segundoNumero = primeiroNumero 
    sequenciaFibonacci.append(proximoNumero)

quantidadeTermos = int(input("Digite a quantidade de termos"))

for indice in range(quantidadeTermos):
    print(sequenciaFibonacci[indice])