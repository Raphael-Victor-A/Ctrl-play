import unittest

# def soma(a,b):             criança
#     return a + b

# class testSoma(unittest.TestCase):

#     def testSomaPositivos(self):
#         self.assertEqual(soma(2,3), 5)

#     def testSomaNegativos(self):
#         self.assertEqual(soma(-2,-3),-5)

#     def testSomasZeros(self):
#         self.assertEqual(soma(0,0),0)

# if __name__ == '__main__':
#     unittest.main()

# def dividir(a,b):
#     if b == 0:
#         raise ValueError("Divisao por zero não permitida")
#     else:
#         return a/b

# class testDividir(unittest.TestCase):

#     def testDivisaoPorZero(self):
#         with self.assertRaises(ValueError):dividir(10,0)

# if __name__ == '__main__':
#     unittest.main()


class calculadora:
    def __init__(self):
        self.resultado = 0

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a , b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisao por zero")
        else:
            return a / b

class testCalculadora(unittest.TestCase):

    def setUp(self):
        self.C = calculadora() 

    def testSoma(self):
        self.assertEqual(self.C.soma(5,3),8)

    def testSubtracao(self):
        self.assertEqual(self.C.subtracao(5,3),2)

    def testMultiplicacao(self):
        self.assertEqual(self.C.multiplicacao(5,3),15)

    def testDivisao(self):
        self.assertEqual(self.C.divisao(5,1),5)
    
    def testDivisaoPorZero(self):
        with self.assertRaises(ValueError): self.C.divisao(10,0)

if __name__ == '__main__':
    unittest.main()