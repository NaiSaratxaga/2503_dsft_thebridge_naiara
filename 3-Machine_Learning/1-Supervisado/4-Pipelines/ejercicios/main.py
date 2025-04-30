import os
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# === 1. Cargar datos igual que cuando entrenaste el modelo ===
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir en entrenamiento y test (aunque solo usaremos test aquí)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# === 2. Cargar el modelo desde la ruta correcta ===
# modelo_path = os.path.join('modelo', 'mejor_modelo_breast_cancer.pkl')
modelo_path = 'C:\\Users\\nsara\\Desktop\\naiara_thebridge\\2503_dsft_thebridge_naiara\\3-Machine_Learning\\1-Supervisado\\4-Pipelines\\ejercicios\\modelo\\mejor_modelo_breast_cancer.pkl'
with open(modelo_path, 'rb') as f:
    modelo_cargado = pickle.load(f)

# === 3. Usar el modelo: hacer predicciones y evaluar ===
predicciones = modelo_cargado.predict(X_test)
print("Accuracy del modelo cargado:", accuracy_score(y_test, predicciones))
