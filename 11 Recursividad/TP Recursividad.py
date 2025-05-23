#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial (num):
    if (num==0) or (num==1):
        return 1
    else:
        return num * factorial (num-1)
        
print (factorial(10))

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def Fibonacci (num):
    if num <= 1:
        return num
    return Fibonacci (num - 1) + Fibonacci (num -2)

print(Fibonacci(4))

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n^m = n ∗ n ^(m−1). Prueba esta función en un algoritmo general.

def potencia (base, exp):
    if exp == 0:    
        return 1
    else:
        return base * potencia (base, exp-1)
print (potencia (3,3))

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def convertidor_decimal_a_binario (num):
    if num == 0:
        return ""
    else:
        return convertidor_decimal_a_binario (num // 2) + str(num % 2)
        
print (convertidor_decimal_a_binario (5))

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def palindromo (palabra):
    if len (palabra) <= 1:
        return True
    if palabra [0] != palabra [-1]:
        return False
    return palindromo (palabra [1:-1])
    
print (palindromo("arañara"))

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n%10) + suma_digitos (n//10)
        
print (suma_digitos (265))

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el 
# siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide 

def contar_bloques(n):
    if n <= 1:
        return n
    else:
        return n + contar_bloques (n-1)
        
print (contar_bloques(8))

#8) Escribí una función recursiva llamada def contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)
        
print (contar_digito(28588578,8))
