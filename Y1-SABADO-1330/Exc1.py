DDD = {61:"Brasilia", 11:"São Paulo", 71:"Salvador"}

iDDD = int(input("Digite o numero do ddd: "))

if iDDD in DDD:
    print(DDD[iDDD])
else:
    print("Não tem no dicionario")

    