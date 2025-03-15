import math

def areaCirculo(raio):
    return math.pi * raio ** 2

def perimetroCirculo(raio):
    return 2 * math.pi * raio

def areaRetangulo(base, altura):
    return base * altura

def perimetroRetangulo(base, altura):
    return 2 * (base + altura)

def areaTriangulo(base, altura):
    return (base * altura) / 2

def perimetroTriangulo(lado1,lado2,lado3):
    return lado1 + lado2 + lado3