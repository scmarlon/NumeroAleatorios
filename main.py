import random
contador = 0
sumatoria = 0
mayor = False
menor = False
iguales = False
sinResultado = False
var = 0
while var < 4:
    numero = random.randint(1, 10)
    print(numero)
    if(var < 3):
        if(numero < 5):
            contador+=1
            var += 1
        if(numero >= 5):
            sumatoria = sumatoria+numero
            var += 1
    else:
        print(sumatoria, "...", contador)
        divi = sumatoria/contador
        print("La division entre la sumatoria y el contador es: ",divi)
        if(divi < 5 and divi > 0):
            menor = True
        if (divi > 5):
            mayor = True
        if (divi == 5):
            iguales = True
        if (divi == 0):
            sinResultado = True
        break