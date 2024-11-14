#Listas são multiplos objetos dentro de apenas um local

convidados = ["raphael", "cleiton", "jorge", "joao"]

print(convidados[0])

print(convidados)

#alteração de objeto pelo indice

convidados[0] = "beatriz"

print(convidados[0])

print(convidados)

##ADICIONANDO ITENS EM LISTA

convidados.append("Joca")

print(convidados)

##INSERINDO EM UMA POSIÇÃO ESPECIFICA

convidados.insert(0, "Savio")

print(convidados)

##REMOVENDO CONVIDADO

convidados.pop()

print(convidados)

##REMOVENDO CONVIDADO DE POSIÇÃO ESPECIFICA

del convidados[0]

print(convidados)

##ORGANIZANDO LISTA

convidados.sort()

print(convidados)

##ORGANIZANDO LISTA EM ORDEM INVERSA

convidados.sort(reverse = True)

print(convidados)

##FUNÇÃO LENGHT

print(len(convidados))

##FUNÇÃM SUM
lista = [1,2,3,4,5,6,7,8,9,10]

soma = sum(lista)

print(soma)

# MATRIZES

timexPessoas = [["palmeiras", "internacional", "corinthians"], ["jose", "maria", "paulo"]]

print(timexPessoas[1][2])

