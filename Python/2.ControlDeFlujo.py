#CONTROL DE FLUJO-----------------------------------

#OR----Al menos una condición debe cumplirse
print(True or True)    #True
print(True or False)   #True
print(False or True)   #True
print(False or False)  #False

#AND----Ambas condiciones deben cumplirse
print(True and True)    #True
print(True and False)   #False
print(False and True)   #False
print(False and False)  #False

#XOR----Una condición debe ser false
print(True ^ True)     #False
print(True ^ False)    #True
print(False ^ True)    #True
print(False ^ False)   #False

if True:
    print("Esto se ejecuta si la condición se cumple")
#----------------------------------------------------------------

if False:
    print("Esto nunca se ejecutará")
elif True:
    print("En caso de que no se cumpla la primera condicion puede ponerse una segunda")
else:
    print("Esto se ejecutaría si ninguna de las anteriores condiciones se cumple")

#CONDICIÓN-BUCLE WHILE

contador=1

while contador<=10:
    print("Se ejecutarán estas acciones")
    contador += 1

#Palabras reservadas break y continue

contadorBreak=1

while contadorBreak<=10:
    print("Se ejecutarán estas acciones")
    if contadorBreak==5:
        ("Si se cumple esta condición el bucle se rompe")
        break
    contadorBreak += 1


contadorContinue=0

while contadorContinue<=10:
    contadorContinue+=1
    if contadorContinue%2==0:
        print(contadorContinue, "Es un número par")
        continue

    print("Esto solo se ejecuta si el contador es impar, por lo tanto no se dispara el continue:",contadorContinue)

#Bucles for
lista=["a", 2,3,5,6]

for elemento in lista:
    print(elemento)      #Recorrer una lista

#-----------------------
if "a" in lista:
    print("a está en la lista") #Recorrer una lista con una condición. También puede hacerse como negación con "not in"

#-----------------------
ordenar= [5,6,8,7,1,2,4,3]

print(sorted(ordenar)) #Ordenar una lista

print(sorted(ordenar, reverse=True)) #Ordena una lista en reversa

