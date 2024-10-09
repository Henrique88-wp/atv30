# crie uma funcao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print("aprovado")
    else:
        print("reprovado")

    return media


n1 = float(input("digite a nota:"))
n2 = float(input("digite a nota:"))
n3 = float(input("digite a nota:"))

resultado = media(n1, n2, n3)
print(resultado)