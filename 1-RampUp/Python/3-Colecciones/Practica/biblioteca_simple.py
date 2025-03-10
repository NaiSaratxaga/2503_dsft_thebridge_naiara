#primero los import de un fichero ejecutable
import os
import time
# Después lasfunciones

# Función para imprimir un libro. He hecho esta función para evitar código repetido
# La función recibe un diccionario con la información de un libro y la imprime por pantalla
def imprimir_libro(libro):
    print(f"📖 Titulo: {libro['Titulo']}")
    print(f"✍️ Autor: {libro['Autor']}")
    print(f"🔑 Alquilado: {libro['Alquilado']}")
    print("-------------------")

# Función para buscar un libro por título. Devuelve el libro si lo encuentra, None si no lo encuentra
# La función recibe una lista de libros y el título del libro a buscar
def buscar_libro_por_titulo(libros, titulo):
    for libro in libros:
        if libro["Titulo"] == titulo:
            return libro
    return None

# Función para imprimir los libros (1-Visualizar)
def imprimir_libros(libros):
    for libro in libros:
        imprimir_libro(libro)
        
# Función para buscar un libro (2-Buscar)
def buscar_libros(libros):   
    titulo_buscar = input("🔍 Introduce el título por favor:")
    libro_buscado = buscar_libro_por_titulo(libros, titulo_buscar)
    
    if libro_buscado:
        print("Libro encontrado")
        imprimir_libro(libro_buscado)
    else:
        print(f"📚 Libro no encontrado en la biblioteca ({titulo_buscar})")
 

# Función para añadir libro (3-Añadir)
# Añadir libro por parte del usuario, tenemos que hacer dentro de la función 2 inputs para que el usuario meta
# el titulo y el autor del libro nuevo
def anadir_libro(libros):   
    # Pedir título y autor al usuario
    titulo = input("📖 Introduce el título del libro:")
    autor = input("✍️ Introduce el autor del libro:")
    
    # Crear un diccionario con la información del nuevo libro
    libro_nuevo = {"📖 Titulo": titulo, "✍️ Autor": autor, "🔑 Alquilado": False}
    
    # Añadir el libro nuevo a la lista de libros
    libros.append(libro_nuevo)
  
    # Mostrar mensaje de confirmación
    print("✅ Se ha añadido un nuevo libro a la biblioteca")
    imprimir_libro(libro_nuevo)
    
# Función para eliminar libro (4-Eliminar)
def eliminar_libro(libros):   
    titulo_buscar = input("🔑 Introduce el libro que quieres eliminar:")
    libro_buscado = buscar_libro_por_titulo(libros, titulo_buscar)
    if libro_buscado:
        libros.remove(libro_buscado)
        print(f"✅ Libro eliminado ({titulo_buscar})")
    else:
        print(f"❌ Libro no encontrado para eliminar ({titulo_buscar})")
    
# función alquilar libro (5-Alquilar)
def alquilar_libros(libros):   
    titulo_buscar = input("🔑 Introduce el libro que quieres alquilar:")
    libro_buscado = buscar_libro_por_titulo(libros, titulo_buscar)
    if libro_buscado:
        libro_buscado["Alquilado"] = True
        print(f"✅ Libro alquilado ({titulo_buscar})")
    else:
        print(f"❌ Libro no encontrado para alquilar ({titulo_buscar})")

# función devolver libro (6-Devolver)
def devolver_libros(libros):   
    titulo_buscar = input("🔄 Introduce el libro que quieres devolver:")
    libro_buscado = buscar_libro_por_titulo(libros, titulo_buscar)
    if libro_buscado:
        libro_buscado["Alquilado"] = False
        print(f"✅ Libro devuelto ({titulo_buscar})")
    else:
        print(f"❌ Libro no encontrado para devolver ({titulo_buscar})")
        
# Creamos una variable para controlar si el usuario quiere salir del programa
        
# Ahora veremos el resto del código del programa
    
# Primero presentamos al usuario las opciones que tendrá disponible
print("👋 Hola, ¿Qué operación quieres realizar?")
print("🔢 Opciones disponibles:")
print()
print("1️⃣ Visualizar todos los libros de la biblioteca")
print("2️⃣ Buscar un libro por título")
print("3️⃣ Añadir un libro")
print("4️⃣ Eliminar un libro por título")
print("5️⃣ Alquilar un libro por título")
print("6️⃣ Devolver un libro por título")
print("➡️ Salir")
print()

libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

# Programa principal
# Bucle para que el usuario pueda realizar las operaciones que desee
salir = False
while not salir:
    opcion = input(" Visualizar / Buscar / Añadir / Eliminar / Alquilar / Devolver / Salir ")
    # Convertimos la opción a minúsculas para que no haya problemas si el usuario escribe en mayúsculas
    opcion = opcion.lower()
    # Dependiendo de la opción que haya elegido el usuario, llamamos a la función correspondiente
    # En este caso, he hecho una función para cada opción.
    match opcion:
        case "visualizar":
            imprimir_libros(libros)
        case "buscar":
            buscar_libros(libros)
        case "añadir":
            anadir_libro(libros)
        case "eliminar":
            eliminar_libro(libros)
        case "alquilar":
            alquilar_libros(libros)
        case "devolver":
            devolver_libros(libros)
        case "salir":
            salir = True
    time.sleep(20)
    os.system("cls")