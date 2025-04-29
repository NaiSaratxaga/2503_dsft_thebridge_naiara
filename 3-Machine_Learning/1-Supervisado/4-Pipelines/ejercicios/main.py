import pickle

# Ruta al archivo .pkl
with open('C:\Users\nsara\Desktop\naiara_thebridge\2503_dsft_thebridge_naiara\3-Machine_Learning\1-Supervisado\4-Pipelines\ejercicios\modelo\mejor_modelo_breast_cancer.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Usar el modelo cargado para hacer predicciones
# Ejemplo con un dato de prueba
import numpy as np
sample = np.array([[14.0, 20.0, 90.0, 600.0, 0.1, 0.2, 0.3, 0.2, 0.3, 0.1,
                    0.5, 1.0, 4.0, 50.0, 0.01, 0.05, 0.06, 0.02, 0.02, 0.005,
                    16.0, 30.0, 110.0, 800.0, 0.13, 0.4, 0.45, 0.2, 0.4, 0.1]])
prediction = modelo.predict(sample)
print("Predicción:", prediction)


