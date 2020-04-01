def media_suicida (mediaProvas, mediaTrabalhos):
    if mediaProvas >= 5 and mediaTrabalhos >= 5:
        mediaFinal = mediaProvas * 0.6 + mediaTrabalhos * 0.4
    elif mediaProvas < 5 or mediaTrabalhos < 5:
        mediaFinal = min(mediaProvas, mediaTrabalhos)

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

mediaProva = sum(notasProva) / quantidadeProva
mediaTrabalho = sum(notasTrabalho) / quantidadeTrabalho

print("Media final = {}".format(media_suicida(mediaProva, mediaTrabalho)))