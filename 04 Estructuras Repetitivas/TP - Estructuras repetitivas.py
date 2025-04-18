# 1) Crea un programa que imprima en pantalla todos los números enteros 
# desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

CORTE = 100
for i in range (CORTE+1):
    print (i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la 
# cantidad de dígitos que contiene.

numero= int (input ("Ingrese un numero entero: "))
cont= 0
resto= numero
while resto > 0:
    resto //= 10
    cont +=1
print ("la cantidad de digitos del numero ingresado es",cont)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre
# dos valores dados por el usuario, excluyendo esos dos valores.

print ("ingrese el rango de numeros")
num1 = int (input ("ingrese primer numero"))
num2 = int (input ("ingrese segundo numero"))
suma = 0
for i in range ((num1 + 1),num2):
    suma += i
print ("la suma total de los numeros comprendidos en el rango es:",suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume 
# en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el 
# usuario ingrese un 0.

num = int (input("Ingrese numero entero a sumar"))
suma = 0
while num != 0:
    suma +=num
    num = int (input("Ingrese numero entero a sumar"))
print ("el total acumulado es:",suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar 
# el número.

import random
num= int (input("Ingrese numero para adivinar: "))
num_aleatorio= random.randint(1,9)
contador=1
while num != num_aleatorio:
    contador +=1
    num= int (input("Ingrese numero para adivinar"))
print ("adivinaste el numero en", contador, "intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares 
# comprendidos entre 0 y 100, en orden decreciente.

for x in range (100,0,-2):
    print (x)

# 7) Crea un programa que calcule la suma de todos los números comprendidos 
# entre 0 y un número entero positivo indicado por el usuario.

num= int (input("ingrese numero entero y positivo"))
suma=0
if num >= 0:
    for x in range (num):
        suma += x      
else:
    print ("No ingreso un numero positivo")
if num >= 0:
    print ("la suma total es:",suma)  

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CONSTANTE_NUM = 5 #constante para reemplazar por 100
num_pares=0
num_impares=0
num_positivos=0
num_negativos=0
for x in range (CONSTANTE_NUM):
    numero= int (input("Ingrese numero entero a evaluar: "))
    if numero %2 == 0:
        num_pares +=1
    else:
        num_impares +=1
    if numero >= 0:
        num_positivos +=1
    else:
        num_negativos +=1
print ("en el rango informado, tenemos: ")
print (num_pares,"numeros pares", num_impares, "numeros impares", num_positivos, "numeros positivos y", num_negativos, "numeros negativos)")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

CONSTANTE_NUM = 5 #constante para reemplazar por 100
suma=0
for x in range (CONSTANTE_NUM):
    numero= int (input("Ingrese numero entero a evaluar: "))
    suma += numero
media = suma / CONSTANTE_NUM
print ("La media de los valores ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero= int (input ("ingrese numero entero: "))
numero_abs= abs(numero)
num_invertido = 0

while numero_abs>0:
    ultimo_dig= numero_abs % 10
    num_invertido= num_invertido*10 + ultimo_dig
    numero_abs= numero_abs// 10
if numero<0:
    num_invertido= -num_invertido
print ("el numero invertido es:", num_invertido)