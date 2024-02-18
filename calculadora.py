# 1.Elabore una calculadora en Python que realice las operaciones de sumar, 
# restar, multiplicar, dividir, calcule la raíz cuadrada. 
# Considere las entradas de solo números (enteros y decimales sin el uso de “e”).

import math
import re

#Expresión Regular de los números permitidos
numero = re.compile(r'\d*\.?\d+')

def suma():
    numeros = solicitar_dos_numeros()
    suma = numeros[0] + numeros[1]
    print("El total es: " + str(suma))

def resta():
    numeros = solicitar_dos_numeros()
    res = numeros[0] - numeros[1]
    print("El total es: " + str(res))

def multiplicacion():
    numeros = solicitar_dos_numeros()
    mult = numeros[0] * numeros[1]
    print("El total es: " + str(mult))

def division():
    numeros = solicitar_dos_numeros()
    div = numeros[0] / numeros[1]
    print("El total es: " + str(div))

def raiz_cuadrada():    
    correcto = False
    while correcto != True:
        num = input("Ingrese un número: ")
        if numero.fullmatch(num):
            correcto = True
        else:
            print("El numero no debe tener el caracter \"e\" o ingreso un caracter inválido, intente de nuevo.")

    print("La raiz cuadrada es: " + str(math.sqrt(float(num))))

def solicitar_dos_numeros():
    numeros = []

    for i in range(2):
        correcto = False
        while correcto != True:
            num1 = input("Ingrese un número: ")
            if numero.fullmatch(num1):
                numeros.append(int(num1))
                correcto = True
            else:
                print("El numero no debe tener el caracter \"e\" o ingreso un caracter inválido, intente de nuevo.")
    return numeros
    
#Diccionario de Operaciones
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: raiz_cuadrada
}

#Menú
print("Seleccione la operacion a realizar: ")
print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Raiz Cuadrada \n6. Salir")
opcion = int(input("Ingrese su selección: "))

while opcion != 6:
    ejecutar = operaciones.get(opcion)
    ejecutar()
    
    print("\n\nSeleccione la operacion a realizar: ")
    print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Raiz Cuadrada \n6. Salir")
    opcion = int(input("Ingrese su selección: "))
else:
    print("Adiós.")