import math

# ejercicio 1
def numero_a_dia(numero):
# Definimos un diccionario con los días de la semana
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    # Devolvemos el valor correspondiente al número
    # usamos el método get() para devolver un valor por defecto
    # en caso de que el número no exista en el diccionario, en este caso devolvemos "Número inválido"
    return dias.get(numero, "Número inválido")

    # aquí llamamos a la función con algún número
numero_a_dia(2)  

# ejercicio 2
""" #Implementa un programa que imprima por pantalla el siguiente patrón

#5 4 3 2 1 

#4 3 2 1 

#3 2 1 

#2 1 

# """

""" n = 5 #Inicializamos n con 5 para que el patrón tenga 5 lineas

for i in range(n, 0, -1): #Este bucle externo controla el número de filas en el patrón.
#range(n, 0, -1) El rango comienza en n y termina en 0, disminuyendo en 1 en cada iteración.
#El tercer parámetro,step, -1, indica que el rango debe ser decreciente.i tomará los valores: 5, 4, 3, 2, 1 en cada iteración.
    for j in range(i,0,-1): #con este bucle recorremos las columnas de i a 0. -1 es el valor de decreciente       
        print( j, end=" ") #imprime el valor de j en la misma línea, el end hace que estén en la misma línea
    print("") #imprime una nueva línea después de imprimir todos los números de la fila
print()
 """

#Crea una función que replique el comportamiento de la pirámide que hicimos 
# en el ejercicio de patrones, pero en este caso, la pirámide debe estar invertida, 
# Para ello voy a meter el código anterior en una función llamada piramide_invertida(n)


def piramide_invertida(n):
    for i in range(n, 0, -1):  # Controla las filas, decreciendo desde n hasta 1
        for j in range(i, 0, -1):  # Controla las columnas, decreciendo desde i hasta 1
            print(j, end=" ")  # Imprime los números en la misma línea
        print()  # Salto de línea al final de cada fila

# Ejemplo de uso:
piramide_invertida(5)

# ejercicio 3
# función que compare 2 números
def comparar_numeros(a, b):
# Comparamos los números y que sean iguales
# que el primero sea mayor que el segundo
# que el segundo sea mayor que el primero
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Los números son iguales"

# Llamamos a la función con los números 5 y 5
comparar_numeros(8, 23) 

# ejercicio 4
#función que sea un contador de letras. Tenemos que pasar 2 argumentos, un texto y una letra a conter
def contador_letras(texto, letra):
    # Devolvemos el número de veces que aparece la letra en el texto
    # Voy a usar el método count() de las cadenas de texto
    return texto.lower().count(letra.lower())
contador_letras("Hola mundo cruel", "o")  

# ejercicio 5
# Función con un único argumento, que sea un string. La salida tiene que ser un diccionario
# con el recuento de cada letra en el string.
def contar_letras(texto):
    # Inicializamos un diccionario vacío
    recuento = {}
    # Recorremos cada letra en el texto
    for letra in texto:
        # Si la letra no está en el diccionario, la añadimos
        if letra not in recuento:
            recuento[letra] = 1
        else:
            # Si la letra ya está en el diccionario, incrementamos su recuento
            recuento[letra] += 1
    return recuento

# Llamamos a la función 
contar_letras("Factorial of a number")
# Debería devolver un diccionario con el recuento de cada letra en el texto

# ejercicio 6
#Función que reciba una lista, un comando y un elemento.
#Si el comando es "add", añadir el elemento a la lista.
#Si el comando es "remove", eliminar el elemento de la lista.
def mi_funcion(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
        else:
            print(f"El elemento {elemento} no está en la lista.")
    return lista

# Aquí añadimos un elemento a la lista
mi_lista = [1, 2, 5, 6, 8, 9, 2]
mi_lista = mi_funcion(mi_lista, "add", 25)
print(mi_lista) 

# Aquí eliminamos un elemento de la lista
mi_lista = mi_funcion(mi_lista, "remove", 23)
print(mi_lista)


# ejercicio 7
#Función que reciba una lista, un comando y un elemento.
#Si el comando es "add", añadir el elemento a la lista.
#Si el comando es "remove", eliminar el elemento de la lista.
def mi_funcion(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
        else:
            print(f"El elemento {elemento} no está en la lista.")
    return lista

# Aquí añadimos un elemento a la lista
mi_lista = [1, 2, 5, 6, 8, 9, 2]
mi_lista = mi_funcion(mi_lista, "add", 25)
print(mi_lista) 

# Aquí eliminamos un elemento de la lista
mi_lista = mi_funcion(mi_lista, "remove", 23)
print(mi_lista)

# ejercicio 8

# ejercicio 9

# Definimos una función que calcule el área de un cuadrado, de un triángulo y de un círculo
# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado ** 2

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * (radio ** 2)
# Dos círculos de radio 10 + un triángulo de base 3 y altura 7
area_circulo(10) + area_circulo(10) + area_triangulo(3, 7)  

# Un cuadrado de lado = 10 +
# 3 círculos (uno de radio = 4 y los otros dos de radio = 6)
# + 5 triángulos de base = 2 + altura = 4
# Cálculo del primer caso: Dos círculos de radio 10 + un triángulo de base 3 y altura 7
area_total_1 = (2 * area_circulo(10)) + area_triangulo(3, 7)
print(f"Área total del primer caso: {area_total_1:.2f}")

# Cálculo del segundo caso: Un cuadrado de lado 10 + 3 círculos (uno de radio 4 y dos de radio 6) + 5 triángulos de base 2 y altura 4
area_total_2 = (area_cuadrado(10)) + (area_circulo(4) + 2 * area_circulo(6)) + (5 * area_triangulo(2, 4))
print(f"Área total del segundo caso: {area_total_2:.2f}")


