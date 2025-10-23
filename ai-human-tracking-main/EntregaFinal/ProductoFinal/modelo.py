import cv2 
import mediapipe as mp
import numpy as np
import joblib
import os

import os
import sys
from pathlib import Path

# --- Configuración de rutas relativas ---
def get_base_path():
    """Devuelve la ruta base del proyecto (donde está el .joblib)"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        # En desarrollo normal, usa el directorio del script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return base_path

# Ruta al modelo (relativa al directorio del script)
model_path = os.path.join(get_base_path(), 'modelo_postura_produccion.joblib')

# --- Carga del Modelo (con verificación) ---
try:
    print(f"Buscando modelo en: {model_path}")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No se encontró el modelo en {model_path}")
        
    modelo = joblib.load(model_path)
    print(f"Modelo cargado exitosamente. Espera {modelo.n_features_in_} características")
    
except Exception as e:
    print(f"ERROR al cargar el modelo: {str(e)}")
    print("Directorios disponibles:")
    print("\n".join(os.listdir(get_base_path())))
    exit()

# --- 2. Inicializar MediaPipe Pose ---
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Agrupaciones de puntos por región
REGIONES = {
    "cara": list(range(0, 10)),
    "mano_izquierda": [15, 17, 19, 21],
    "mano_derecha": [16, 18, 20, 22],
    "pie_izquierdo": [27, 29, 31],
    "pie_derecho": [28, 30, 32]
}

# Índices de landmarks a excluir
excluded_indices = list(range(0, 10)) + [15, 17, 19, 21, 16, 18, 20, 22, 27, 29, 31, 28, 30, 32]

# Función para calcular promedio de una región
def get_avg(landmarks, indices):
    x = np.mean([landmarks[i].x for i in indices])
    y = np.mean([landmarks[i].y for i in indices])
    z = np.mean([landmarks[i].z for i in indices])
    return x, y, z

def extraer_features_42(results):
    """
    Extrae las 42 características exactamente como en el script de recolección de datos.
    """
    if not results.pose_landmarks:
        return None
        
    landmarks = results.pose_landmarks.landmark
    row = []

    # 1. Agregar los landmarks no excluidos (torso, hombros, etc.)
    for i in range(33):
        if i not in excluded_indices:
            row.extend([landmarks[i].x, landmarks[i].y, landmarks[i].z])

    # 2. Agregar los promedios para las regiones
    for region, indices in REGIONES.items():
        x, y, z = get_avg(landmarks, indices)
        row.extend([x, y, z])
    
    return np.array(row).reshape(1, -1)

# --- 4. Abrir Cámara y Bucle Principal ---
cap = cv2.VideoCapture(0)
print("\nIniciando cámara... Presiona 'q' en la ventana para salir.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar la imagen para detectar la pose
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)
    frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

    # Dibujar el esqueleto
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Extraer las características usando la lógica original
    features = extraer_features_42(results)

    # Si se detecta una pose y las features coinciden, predecir
    if features is not None and features.shape[1] == modelo.n_features_in_:
        try:
            prediccion = modelo.predict(features)[0]
            probabilidad = modelo.predict_proba(features).max()

            texto_prediccion = f'{prediccion.upper()} ({probabilidad:.2f})'
            cv2.putText(frame, texto_prediccion, (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except Exception as e:
            print(f"Error durante la predicción: {e}")
            
    else:
        cv2.putText(frame, "POSTURA NO DETECTADA", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar el frame
    cv2.imshow('Reconocimiento de Postura - Modelo Original', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# --- 5. Limpieza ---
print("Cerrando aplicación.")
cap.release()
cv2.destroyAllWindows()