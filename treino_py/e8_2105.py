def media(a,b):
    m = ( a + b ) / 2
    return media

def classificaMedia(a):
    if (a > 9.0 and a <= 10.0):
        return "A"
    elif (a > 7.5 and a <= 9.0):
        return "B"
    elif (a > 6.0 and a <= 7.5):
        return "C"
    elif (a > 4.0 and a <= 6.0):
        return "D"
    else:
        return "E"

def aprovacao(a):
    dic = {"A":"Aprovado", "B":"Aprovado", "C":"Aprovado", "D":"Aprovado", "E":"Aprovado"}
    return dic[a]

nota1 = float(input("Entre com a nota 1 : "))
nota2 = float(input("Entre com a nota 2 : "))

print(aprovacao(classificaMedia(media(nota1, nota2))))

