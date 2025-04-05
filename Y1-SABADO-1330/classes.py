# class pets:
#     def __init__(self, nome):
#         self.nome = nome
#         self.energia = 100
    
#     def comer(self):
#         self.energia += 10
#         print(f"{self.nome} comeu e ganhou energia! energia atual: {self.energia}")
    
#     def brincar(self):
#         if self.energia >= 20:
#             self.energia -= 15
#             print(f"{self.nome} brincou e gastou energia! energia atual: {self.energia}")
#         else:
#             print(f"{self.nome} está cansado e precisa comer!")

# pet1 = pets("Mavie")
# pet2 = pets("blade")
# pet3 = pets("mel")

# pet1.comer()


#-----------------------------------------------------------


# class casa():
#     def __init__(self, rua, numero, cep):
#         self.rua = rua
#         self.numero = numero
#         self.cep = cep

#     def enderecoCompleto(self):
#         print(f"Endereço completo: {self.rua}, {self.numero}, {self.cep}")

# casa1 = casa(rua = "adolino", numero = "25", cep = "000.000-00")
# casa2 = casa(rua = "patolino", numero = "35", cep = "000.000-00")

# casa1.enderecoCompleto()
# casa2.enderecoCompleto()

#-----------------------------------------------------------


# class retangulo():
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def calcularArea(self):
#         return self.base * self.altura
    
#     def calcularPerimetro(self):
#         return 2 * (self.base+ self.altura)
    
# base = float(input("Digite o valor da base: "))
# altura = float(input("Digite o valor da altura: "))

# retangulo = retangulo(base, altura)

# while True:
#     print("1 - AREA")
#     print("2 - PERIMETRO")
#     opcao = int(input("Digite a opção que você quer: "))

#     if opcao == 1:
#         print(f"Area: {retangulo.calcularArea()}(m^2)")

#     elif opcao == 2:
#         print(f"Perimetro: {retangulo.calcularPerimetro()}(m)")
    
#     else:
#         print("Não existe essa opção!")
#         break

#-----------------------------------------------------------