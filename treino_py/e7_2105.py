numero = int(input("Entre com um inteiro : "))

fatorial = 1
for i in range (1, numero + 1, 1):
    fatorial = fatorial*i

print("O fatorial de %d é %d : " %(numero, fatorial))
