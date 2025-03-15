import geometria as g

def menu():
    print("🧮Calculadora geométrica🧮")
    print("1 - Área do Círculo")
    print("2 - Perímetro do Círculo")
    print("3 - Área do Retângulo")
    print("4 - Perímetro do Retângulo")
    print("5 - Área do Triângulo")
    print("6 - Perímetro do Triângulo")
    print("0 - SAIR❌")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        raio = float(input("Raio: "))
        print(f"Área: {g.areaCirculo(raio)}")
    
    elif opcao == 2:
        raio = float(input("Raio: "))
        print(f"Perímetro: {g.perimetroCirculo(raio)}")
        
    elif opcao == 3:
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        print(f"Perímetro: {g.areaRetangulo(base, altura)}")
    
    elif opcao == 4:
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        print(f"Perímetro: {g.perimetroRetangulo(base, altura)}")
    
    elif opcao == 5:
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        print(f"Perímetro: {g.areaTriangulo(base, altura)}")

    elif opcao == 6:
        lado1 = float(input("Lado 1:"))
        lado2 = float(input("Lado 2:"))
        lado3 = float(input("Lado 3:"))


        print(f"Perímetro: {g.perimetroTriangulo(lado1,lado2,lado3)}")