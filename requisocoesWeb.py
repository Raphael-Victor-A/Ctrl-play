import requests
from bs4 import BeautifulSoup

print("\nConectando ao site")

url = "https://www.uol.com.br"
resposta = requests.get(url)

if resposta.status_code == 200:
    print("Conexao bem-sucedida!")
else:
    print("Conexao mal-sucedida. Codigo do erro:", resposta.status_code)
    exit()

print("\nAnalisando a estrutura do site!")

soup = BeautifulSoup(resposta.text, "html.parser")

pageTitle = soup.title.string
print(f"exibindo titulo da pagina: {pageTitle}")


print("\nProcurando os titulos das noticias")

titles = soup.find_all(["h2","h3"])

print("\n===========titulos enumerados============")
for i, titles in enumerate(titles, 1):
    print(f"{i}.{titles.get_text(strip = True)}")
