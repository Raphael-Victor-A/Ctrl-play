# nome = "Raphael"
# sobrenome = "Victor@..."

# print(nome + sobrenome)

# print("Raphael \t\nVictor \t\t\neh \tprofessor")

# print(len(sobrenome))
# print(sobrenome.find("@"))
# print(sobrenome.count("."))

email = input("Escreva seu email: ")

print(email)
print("Quantidade de caracteres no email: ", len(email))

if email.find("@") != -1:
    print("confirmado")
else:
    print("recusado")
