import dicionario

def enforcado(num_erros):
    if num_erros < 6:
        return False
    else:
        return True

def codifica(palavra):
    resp = ""
    for c in palavra:
        resp = resp + "_ "
    return resp    

def acertou(pal):
    if "_" in pal:
        return False
    else:
        return True    

def chuta(secret, word, letter):
    i  = 0
    resp = ""
    while i < len(word):
        if word[i] == letter:
            resp = resp + letter + " "
        else:
            resp = resp + secret[2*i] + " "
        i = i + 1
    return resp            

palavra = dicionario.sorteio('geografia').lower()

# print(palavra)
num_erros = 0
segredo = codifica(palavra)

segredo = chuta(segredo, palavra, ' ')

while not enforcado(num_erros) and not acertou(segredo):
    #imprime a tela do jogo
    print(segredo)
    print("erros: ", num_erros)
    
    #pede para usuario digitar letra
    letra = input("Informe uma letra: ")
    
    #atualiza jogo com a letra digitada
    if not letra in palavra:
        num_erros = num_erros + 1
    else:
        segredo = chuta(segredo, palavra, letra)        

if enforcado(num_erros):
    print("Você não acertou a palavra")
    print(palavra)
else:
    print("Parabéns, você acertou!")
    print(segredo)
