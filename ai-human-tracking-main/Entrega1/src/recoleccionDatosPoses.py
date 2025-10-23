import cv2
import mediapipe as mp
import csv
import numpy as np

#En este proyecto se utilizo IA generativa para:
#optimizar el código inicial
#conocer y utilizar mediapipe
#como sacar los promedios de las partes promediables como las manos, pies y cara

# Ruta del video y archivo de salida
video_path = r"" #Poner la ruta del video
csv_path = r"" #Poner la ruta de donde se guarda el archivo


# Configuración de MediaPipe Pose
mp_pose = mp.solutions.pose 
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Agrupaciones de puntos por región
REGIONES = {
    "cara": list(range(0, 10)),  # Nariz, ojos, orejas, etc.
    "mano_izquierda": [15, 17, 19, 21],  # Muñeca y dedos izquierdos
    "mano_derecha": [16, 18, 20, 22],    # Muñeca y dedos derechos
    "pie_izquierdo": [27, 29, 31],       # Tobillo, talón, punta del pie izquierdos
    "pie_derecho": [28, 30, 32]          # Tobillo, talón, punta del pie derechos
}

# Índices de landmarks a excluir (cara, manos, pies)
excluded_indices = list(range(0, 10)) + [15, 17, 19, 21, 16, 18, 20, 22, 27, 29, 31, 28, 30, 32]

# Función para calcular promedio de una región
def get_avg(landmarks, indices):
    x = np.mean([landmarks[i].x for i in indices])
    y = np.mean([landmarks[i].y for i in indices])
    z = np.mean([landmarks[i].z for i in indices])
    return x, y, z

# Inicializar video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

# CSV
f = open(csv_path, 'w', newline='')
writer = csv.writer(f, delimiter=';')

# Header: primer columna 'segundo' y coordenadas de landmarks no excluidos
header = ['segundo']
for i in range(33):  # 33 es el total de landmarks en MediaPipe
    if i not in excluded_indices:
        header.extend([f'landmark_{i}_x', f'landmark_{i}_y', f'landmark_{i}_z'])

# Añadir encabezados para las regiones promediadas
for region in REGIONES:
    header.extend([f'{region}_prom_x', f'{region}_prom_y', f'{region}_prom_z'])

# Escribir encabezados en el archivo CSV
writer.writerow(header)

frame_num = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_num += 1
    seconds = frame_num / fps

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        h, w, _ = frame.shape
        landmarks = results.pose_landmarks.landmark

        # Dibujar las conexiones de los landmarks
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Fila de datos para el CSV
        row = [round(seconds, 2)]

        # Agregar los landmarks no excluidos (sin cara ni manos)
        for i in range(33):
            if i not in excluded_indices:
                x, y, z = landmarks[i].x, landmarks[i].y, landmarks[i].z
                row.extend([x, y, z])

        # Agregar los promedios para las regiones de la cara y manos
        for region, indices in REGIONES.items():
            x, y, z = get_avg(landmarks, indices)
            row.extend([x, y, z])

        # Escribir la fila en el archivo CSV
        writer.writerow(row)

    # Mostrar el video con los landmarks dibujados
    cv2.imshow('Pose promediada', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
f.close()
cv2.destroyAllWindows()