def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Divisao por zero nao pode!"
    except TypeError:
        return "Os tipos sao invalidos!"
    
print(dividir(10,2))
print(dividir(10,0))
print(dividir(10, 'a'))

class calculadora:
    def __init__(self):
        self.resultado = 0

    def soma(self, a, b):
        try:
            return a + b
        except TypeError:
            return "erro numero"
        
    def subtracao(self, a, b):
        try:
            return a - b
        except TypeError:
            return "erro numero"
        
    
    def multiplicacao(self, a , b):
        try:
            return a * b
        except TypeError:
            return "erro numero"
        
    
    def divisao(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return "divisao por zero"
        except TypeError:
            return "erro de tipo"

c = calculadora()

print(c.soma(1,2))
print(c.soma(1, 'a'))
print(c.subtracao(1,2))
print(c.subtracao(1, 'a'))
print(c.divisao(10,2))
print(c.divisao(10,0))
print(c.divisao(10,'A'))

