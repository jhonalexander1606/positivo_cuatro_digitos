# programa que identifica si un numero es de 4 digitos y positivo o negativo

print("------------------------------------")
print("---numeros positivos de 4 digitos---")
print("------------------------------------")

# input 

x = int(input("inserte un numero" ))

#processing

if (x > 0):
    if (x > 999 and x < 10000):
        print("el numero es positivo y de 4 digitos")
    else :
        print("el numero es positivo pero no es de 4 digitos")

else:
    if x < -999 and x > -10000:
        print("el numero es negativo y de cuatro digitos")

    else:
        print(" el numero es negativo y no es de 4 digitos")
    
