import os
import shutil

print(os.getcwd())

ruta = os.path.join(os.getcwd(), "./2-Data_Analysis/3-Sources/Archivos/Practica/carpeta_ejercicio")


print(f"ruta: {ruta}")


doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')


# Mapeo de carpetas y sus extensiones correspondientes
categories = {
    "Imagenes": img_types,
    "Documentos": doc_types,
    "Software": software_types
}

# Carpeta para archivos que no correspondan a las categorías anteriores
otros_folder = "Otros"

# Crear las carpetas de destino dentro de la carpeta ruta si no existen
for folder in list(categories.keys()) + [otros_folder]:
    target_path = os.path.join(ruta, folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

# Recorrer todos los elementos de la carpeta a la que apunta la variable ruta
for item in os.listdir(ruta):
    item_path = os.path.join(ruta, item)
    
    # Se salta si es una carpeta para evitar mover nuestras propias carpetas destino
    if os.path.isdir(item_path):
        continue
    
    # Obtener la extensión del archivo en minúsculas
    _, ext = os.path.splitext(item)
    ext = ext.lower()

    # Determinar a qué carpeta se debe mover el archivo
    moved = False
    for folder, extensions in categories.items():
        if ext in extensions:
            dest_path = os.path.join(ruta, folder, item)
            shutil.move(item_path, dest_path)
            moved = True
            break

    # Si la extensión no coincide con ninguna categoría, mover a "Otros"
    if not moved:
        dest_path = os.path.join(ruta, otros_folder, item)
        shutil.move(item_path, dest_path)

print("¡Archivos ordenados exitosamente!")