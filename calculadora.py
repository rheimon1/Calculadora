def media_suicida (mediaProvas, mediaTrabalhos):
    if mediaProvas >= 5 and mediaTrabalhos >= 5:
        mediaFinal = mediaProvas * 0.6 + mediaTrabalhos * 0.4
    elif mediaProvas < 5 or mediaTrabalhos < 5:
        if mediaProvas < mediaTrabalhos:
            mediaFinal = mediaProvas
        elif mediaProvas > mediaTrabalhos:
            mediaFinal = mediaTrabalhos
        else:
            mediaFinal = mediaProvas

    return mediaFinal


notasProva = []
notasTrabalho = []

quantidadeProva = int(input("Quantidade de provas: "))

for item in range(quantidadeProva):
    n = float(input("Nota da prova {}: ".format(item + 1)))
    notasProva.append(n)

quantidadeTrabalho = int(input("Quantidade de trabalhos: "))

for item in range(quantidadeTrabalho):
    n = float(input("Nota do trabalho {}: ".format(item + 1)))
    notasTrabalho.append((n))

auxiliar = 0

for item in notasProva:
    auxiliar += item

mediaProva = auxiliar / len(notasProva)

auxiliar = 0

for item in notasTrabalho:
    auxiliar += item

mediaTrabalho = auxiliar / len(notasTrabalho)

print("Media final = {}".format(media_suicida(mediaProva, mediaTrabalho)))