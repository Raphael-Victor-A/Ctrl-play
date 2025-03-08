arquivo = "listaDeCompras.txt"

def adicionarItem():
    item = input("Digite o item a ser adicionado: ")
    with open(arquivo, "a") as arq:
        arq.write(item + "\n")
    print(f"{item} adicionado à lista!")

def visualizarLista():
    try:
        with open(arquivo, "r") as arq:
            itens = arq.readlines()
            if not itens:
                print("Lista está vazia!")
            else:
                print("Sua lista de compras: ")
                for i, item in enumerate(itens, start =1):
                    print(i, item.strip())
    except FileNotFoundError:
        print("A lista não existe!")

def removerItem():
    visualizarLista()
    try:
        num = int(input("Digite o numero do item para remover: ")) - 1
        with open(arquivo, "r") as arq:
            itens = arq.readlines()
        if 0 < num < len(itens):
            itemRemovido = itens.pop(num)
            with open(arquivo, "w") as arq:
                arq.writelines(itens)
            print(f"{itemRemovido.strip()} foi removido!")
        else:
            print("Item não existe!")
    except (ValueError, FileNotFoundError):
        print("Erro ao remover item do sistema!")

while True:
    print("🛒SUA LISTA DE COMPRAS!🛒")
    print("1 - ADICIONAR ITEM🐒")
    print("2 - VISUALIZAR LISTA👁️👁️")
    print("3 - REMOVER ITEM💸")
    print("4 - SAIR❌")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        adicionarItem()
    elif opcao == 2:
        visualizarLista()
    elif opcao == 3:
        removerItem()
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção invalida❌")