#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo ():
    return print ("Hola Mundo!")
imprimir_hola_mundo ()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
#Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return  print(f"Hola {nombre}")

nombre = input("Ingrese nombre: ")
saludar_usuario (nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) 
#que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido,edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") 

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
edad = input("Ingrese edad: ")
residencia = input("Ingrese residencia: ")
informacion_personal (nombre, apellido,edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
#el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
#devuelva el perímetro del círculo. Solicitar el radio
#Perímetro = 2(pi) * radio. 
#Área = pi * radio al cuadrado


def calcular_area_circulo(radio):
    return print("el area es: ", 3.14*(radio**2))
    
def calcular_perimetro_circulo(radio):
    return print("el perimetro es: ",2*3.14*radio)    

radio = float (input("Ingrese radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
    return print("los segundos ingresados equivalen a", segundos/60, "horas")

segundos = int (input("Ingrese segundos: "))
segundos_a_horas(segundos)

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función


def tabla_multiplicar(numero):
    print(f"tabla de multiplicar de {numero}: ")
    for i in range (1,11):
        print (f"{numero} X {i} = {numero*i}")

numero = int (input("Ingrese numero para obtener tabla: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y
#devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.


def operaciones_basicas(a, b):
    print(f"suma de {a} y {b} = ", a+b)
    print(f"resta de {a} y {b} = ", a-b)
    print(f"multiplicacion de {a} y {b} = ", a*b)
    print(f"division de {a} y {b} = ", a/b)

a = int (input("Ingrese primer numero: "))
b = int (input("Ingrese segundo numero: "))
operaciones_basicas(a, b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para 
#mostrar el resultado con dos decimales.
#IMC = Peso / altura**2


def calcular_imc(peso, altura):
    IMC = peso/altura**2
    print ("Su IMC es: ", IMC)

peso = float (input("Ingrese peso en kg: "))
altura = float (input("Ingrese altura em mts: "))
calcular_imc(peso, altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
#Grados Fahrenheit = (grados centígrados × 9/5) +32


def celsius_a_fahrenheit(celsius):
    Fahrenheit = (celsius * (9/5))+32
    print (f"Los {celsius} grados celsius, equivalen a {Fahrenheit:.2f} grados Fahrenheit")

celsius = float (input("Ingrese grados celsius: "))
celsius_a_fahrenheit(celsius)

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    print (f"El promedio de {a}, {b} y {c} es: {promedio}")
    
a= float(input ("Ingrese el 1er numero: "))
b= float(input ("Ingrese el 2do numero: "))
c= float(input ("Ingrese el 3er numero: "))

calcular_promedio(a, b, c)

