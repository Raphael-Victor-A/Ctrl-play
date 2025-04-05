# Uma classe chamada de "Animal" com uma função __init__ com os parâmetros self, nome e idade
# dentro da função, inicializar os parâmetros nome e idade e criar uma variável chamada 
# energia que começa com o valor de 100. 

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100

    def dormir(self, horas):
        energiaGanha = horas * 10
        self.energia = self.energia + energiaGanha
        # self.energia += energiaGanha
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} dormiu por {horas} e ganhou {energiaGanha} de energia. Energia atual: {self.energia}")

    def brincar(self, tempo):
        energiaGasta = tempo * 5
        if self.energia >= energiaGasta:
            self.energia -= energiaGasta
            print(f"{self.nome} brincou por {tempo} minutos e gastou {energiaGasta} de energia. Energia atual: {self.energia}")
        else:
            print(f"{self.nome} está cansado demais para brincar!")

animal1 = Animal("Mavie", 8)

animal1.brincar(10)
animal1.dormir(4)