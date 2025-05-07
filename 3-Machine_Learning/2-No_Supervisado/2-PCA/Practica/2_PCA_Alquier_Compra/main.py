import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

# === 1. Cargar tus datos ===
# Cambia la ruta si el archivo CSV está en otro directorio
# Aquí uso una ruta absoluta para asegurarte de que cargue correctamente el archivo CSV
df = pd.read_csv('data/comprar_alquilar.csv')

# Dividir el DataFrame en características (X) y target (y)
X = df.drop('comprar', axis=1)  # Excluir la columna 'comprar' para obtener las características
y = df['comprar']  # La columna objetivo (target)

# Dividir en entrenamiento y test (80% entrenamiento, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# === 2. Cargar el modelo desde la ruta correcta ===
# Asegúrate de que la ruta del modelo esté bien especificada
modelo_path = 'C:Users\\nsara\\Desktop\\naiara_thebridge\\2503_dsft_thebridge_naiara\\3-Machine_Learning\\2-No_Supervisado\\2-PCA\\Practica\\2_PCA_Alquier_Compra\\modelo\\mejor_modelo.pkl'

# Cargar el modelo con pickle
with open(modelo_path, 'rb') as f:
    loaded_model = pickle.load(f)

# === 3. Usar el modelo: hacer predicciones y evaluar ===
# Realizar predicciones con el modelo cargado
predicciones = loaded_model.predict(X_test)

# Evaluar el modelo usando accuracy_score
print("Accuracy del modelo cargado:", accuracy_score(y_test, predicciones))

