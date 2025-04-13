# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor 
# de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int (input ("ingrese su edad: "))
if (edad>18):
    print ("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o 
# igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso 
# contrario deberá mostrar el mensaje “Desaprobado”.
nota = int (input ("ingrese nota: "))
if nota >=6 :
    print ("aprobado")
else:
    print ("desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

num = int (input ("ingrese numero: "))
if num % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ? Niño/a: menor de 12 años.
# ? Adolescente: mayor o igual que 12 años y menor que 18 años.
# ? Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ? Adulto/a: mayor o igual que 30 años.

edad = int (input ("ingrese edad: "))
if edad<12:
    print ("Niño/a: menor de 12 años.")
elif (edad >=12) and (edad <18):
    print ("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif (edad>=18) and (edad <30):
    print ("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif (edad >=30):
    print ("Adulto/a: mayor o igual que 30 años.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = str (input ("ingrese contraseñas de entre 8 y 14 caracteres: "))
cantidad_caracteres = len (contraseña)
if (cantidad_caracteres >= 8) and (cantidad_caracteres <= 14):
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode (numeros_aleatorios)
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)
if (media>mediana) and (mediana>moda):
    print ("Sesgo positivo o a la derecha:")
elif (media<mediana) and (mediana<moda):
    print ("Sesgo negativo o a la izquierda:")
elif media== (mediana==moda):
    print ("Sin Sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input (str ("ingrese palabra: "))
vocales = "aeiouAEIOU"
ultima_letra = frase [-1]
if ultima_letra in vocales:
    print (frase + "¡")
else:
    print (frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str (input ("Ingrese su nombre: "))
print ("Ingrese 1. Si quiere su nombre en mayúsculas")
print ("Ingrese 2. Si quiere su nombre en minúsculas.")
print ("Ingrese 3. Si quiere su nombre con la primera letra mayúscula")
opcion = int (input ("Ingrese opcion deseada: "))
if opcion == 1:
    texto = nombre.upper()
elif opcion == 2:
    texto = nombre.lower()
elif opcion == 3:
    texto = nombre.title()
print (texto)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int (input ("ingrese magnitud del terremoto: "))
if magnitud < 3:
    texto= "Muy leve(imperceptible)."
elif (magnitud >=3) and (magnitud < 4):
    texto = "Leve (ligeramente perceptible)."
elif (magnitud >=4) and (magnitud < 5):
    texto = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif (magnitud >=5) and (magnitud < 6):
    texto = "Fuerte (puede causar daños en estructuras débiles)."
elif (magnitud >=6) and (magnitud < 7):
    texto = "Muy Fuerte (puede causar daños significativos)."
elif (magnitud >=7):
    texto = "Extremo (puede causar graves daños a gran escala)."
print (texto)

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str (input("Ingrese el hemisferio en que se encuentra N (para norte) o S (para sur): "))
hemisferio_mayus = hemisferio.upper()
mes = int (input ("Ingrese numero de mes, ejemplo use 1 para enero: "))
dia = int (input("Ingrese numemro de dia del mes: "))
if hemisferio_mayus == "N":
    if (mes == 1) or (mes == 2):
        print ("Estas en invierno")
    elif (mes == 4) or (mes == 5):
        print ("Estas en primavera")
    elif (mes == 7) or (mes ==8):
        print ("Estas en verano")
    elif (mes == 10) or (mes ==11):
        print ("Estas en otoño")
    elif (mes == 12):
        if (dia >= 21):
            print ("Estas en invierno")
        else:
            print ("Estas en otoño")
    elif (mes == 3):
        if (dia >= 21):
            print ("Estas en primavera")
        else:
            print ("Estas en invierno")
    elif (mes == 6):
        if (dia >= 21):
            print ("Estas en verano")
        else:
            print ("Estas en primavera")
    elif (mes == 11):
        if (dia >= 21):
            print ("Estas en otoño")
        else:
            print ("Estas en verano")
if hemisferio_mayus == "S":
    if (mes == 1) or (mes == 2):
        print ("Estas en verano")
    elif (mes == 4) or (mes == 5):
        print ("Estas en otoño")
    elif (mes == 7) or (mes ==8):
        print ("Estas en invierno")
    elif (mes == 10) or (mes ==11):
        print ("Estas en primavera")
    elif (mes == 12):
        if (dia >= 21):
            print ("Estas en verano")
        else:
            print ("Estas en primavera")
    elif (mes == 3):
        if (dia >= 21):
            print ("Estas en otoño")
        else:
            print ("Estas en verano")
    elif (mes == 6):
        if (dia >= 21):
            print ("Estas en invierno")
        else:
            print ("Estas en otoño")
    elif (mes == 11):
        if (dia >= 21):
            print ("Estas en primavera")
        else:
            print ("Estas en invierno")
