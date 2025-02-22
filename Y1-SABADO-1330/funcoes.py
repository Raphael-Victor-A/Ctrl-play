def soma(a,b,c):
    return a + b + c

def multi(d,e,f):
    return d*e*f

def bemVindo():
    print("BIEN VINIDO")

def menor(a,b):
    if a <=b:
        return a
    else:
        return b


print(menor(25,15))

# print(multi(4,3,5))
# print(multi(6,7,8))
# print(soma(5,3,4))
# print(soma(5,2,2))

def velocidadeMedia(tempo,distancia):
    return distancia/tempo

distancia = float(input("Digite a distancia: "))
tempo = float(input("Digite o tempo em horas: "))

print(velocidadeMedia(tempo,distancia))
