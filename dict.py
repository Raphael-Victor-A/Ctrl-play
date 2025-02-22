precos = {
    1:4.00,
    2:4.50,
    3:5.00,
    4:2.00,
    5:1.50
}

CodigoProduto = int(input("Digite o codigo do produto: "))

quantidade = int(input("Digite a quantidade desejada:"))

PrecoUnitario = precos[CodigoProduto]

total = PrecoUnitario * quantidade

print(total)