numero = 10

if (numero > 100):
    print("numero maior que 100")
    numero = 100
    if (numero > 150):
        print("numero maior que 150")

elif (numero > 50):
    print("numero maior que 50 e menor que 150")
    numero = 50
else:
    print("numero menor que 100")
    numero = 0

print ("Continue...")
