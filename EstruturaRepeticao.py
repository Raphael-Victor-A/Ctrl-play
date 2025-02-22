# for -> Listas
#while -> Percorrer uma condição

# for num in range(1,1234567890):
#     print(num)

# for letras in "Otorrinolaringologista":
#     print(letras)

# numero = 1 

# while numero <= 5:
#     numero += 1#2 3 4
#     print(numero)#1 2 3


# 1-fazer uma lista de 10 numeros
# 2-inicializar uma soma
# 3-utilizando "for" vcs vao somar a cada looping
# 4-print no total da soma


# numeros = [1,2,3,4,5,6,7,8,9,10]

# soma = 0

# for numero in numeros:
#     soma += numero

# print(soma)


#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.

# numero = float(input("Digite um numero para ver sua tabuado: "))

# print(f"Tabuada do numero {numero}")

# for i in range(1,11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

soma = 0

for numero in range(1,21):
    if numero % 2 != 0:
        soma += numero
        
print(soma)