
def saudacoes_GUI(nome):
    import random
    frases = ["Bom dia, Meu nome é "+ nome +"Como vai voce?", "Olá", "Oi, qual sua pergunta?"]
    print(frases[random.randint(0,2)])


def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavraProibidas = ["idiota", "burro", "bobão", "canalha"]
    for p in palavraProibidas:
        if p in texto:
            print("IXI RAPA, VEM ME OFENDER NÃO")
            return recebeTexto()
        return texto
    
def buscaResposta(nome, texto):
    with open("BaseConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            linha = conhecimento.readline()
            if linha != "":
                if jaccard(texto, linha) > 0.3:
                    proxima_linha = conhecimento.readline()
                    if "Chatbot: " in proxima_linha:
                        return proxima_linha.strip()
            else:
                conhecimento.write(f"\n{nome}: {texto}")
                return "Me desculpe, não sei o que falar"

                

            
def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot", nome)

def salva_sugestao(sugestao):
    with open("BaseConhecimento.txt", "+a") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")

def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavra_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavra_em_comum += 1
        return palavra_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = [ "?", "!", "...", ".", ":", ",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase