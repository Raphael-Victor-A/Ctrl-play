class Casa():
    def __init__(self, rua, bairro, cep, numero):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.numero = numero

    def enderecoCompleto(self):
        return "Endereço completo: " +self.rua+ ", " +self.numero+ ", " +self.bairro+ " - CEP: " +self.cep
    
casa1 = Casa(rua = "Rua Ceara", bairro = "Jardim dos Estados", cep = "3", numero = "0")
casa2 = Casa("Rua Mato Grosso", "Estados dos Jardins", "-2", "PI")

print(casa1.bairro)
print(casa1.enderecoCompleto())

# Fazer os objetos casa2 e casa3 e imprimir a função enderecoCompleto() de cada casa 
# com valores distintos.

