# def saudacao(nomeDeUsuario):
#     print("Ola seja bem vindo a ctrl play" , nomeDeUsuario)

# saudacao("Renan")
# saudacao("raphael")
# saudacao("eduardo")
# saudacao("jose")
# saudacao("joao")

#acima estamos passando uma informação para nossa funcao por um 
#parametro

# def filme(FilmeFav):
#     print("meu filme fav é", FilmeFav)

# FilmeFav = input()

# filme(FilmeFav)

# def soma(a,b):
#     return a + b

# resultado = soma(a=123,b = 321)

# print(resultado)

# def vMedia(distancia, tempo):
#     return distancia/tempo

# distancia = float(input("distancia: "))
# tempo = float(input("tempo: "))

# if tempo > 0:
#     resultado = vMedia(distancia, tempo)
#     print("a velocidade media foi: ", resultado)
# else:
#     print("o tempo tem que ser maior que zero para calcular a vM")

# def Converter(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input())

# fahrenheit = Converter(celsius)
# print("Temperatura convertida em f: ", fahrenheit)


# def soma(a,b):
#     return a+b

# def subtracao(a,b):
#     return a-b

# def calculadora(a,b):
#     print(soma(a,b))
#     print(subtracao(a,b))

# a = int(input())
# b = int(input())

# calculadora(a,b)

def calcular_media(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = calcular_media(nota1,nota2,nota3)

if media >= 7:
    print("o aluno foi aprovado", media)
else:
    print("aluno reprovado", media)
