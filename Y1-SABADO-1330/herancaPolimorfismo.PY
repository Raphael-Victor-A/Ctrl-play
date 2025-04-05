# #encapsulamento 

# class A:
#     a = 1
#     __b = 2

# class B(A):
#     __c = 3

#     def __init__(self):
#         print(self.a)
#         print(self.__c)

# exibirA = A()
# print(exibirA.a) #Exibindo atributo publico da class A
# print(exibirA.__b) # ERRO: atributo privado da class A


class animal:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def emitirSom(self):
        return "Som de animal"
    
    def informacao(self):
        return f"Nome: {self.nome}, idade: {self.idade} anos"
    
class cachorro(animal):
    def emitirSom(self):
        return "Au Au!"

class gato(animal):
    def emitirSom(self):
        return "Miauuuu"

animal1 = cachorro("Rex", 25)
animal2 = gato("Marie", 32) 

print(animal1.informacao())
print(animal1.emitirSom())


print(animal2.informacao())
print(animal2.emitirSom())