# 🧠 AI Human Tracker

Un sistema de **reconocimiento de actividades humanas** basado en **visión por computadora** y **aprendizaje automático supervisado**, desarrollado como proyecto académico en la Universidad Icesi.  
El modelo identifica acciones humanas como **caminar hacia o lejos de la cámara, girar, sentarse y ponerse de pie**, utilizando articulaciones clave del cuerpo detectadas con **MediaPipe**.

---

## 🚀 Objetivo
Desarrollar un modelo de inteligencia artificial capaz de reconocer y clasificar actividades humanas a partir de coordenadas de articulaciones corporales, demostrando cómo la **calidad del etiquetado de datos** influye directamente en el desempeño de modelos de visión artificial.

---

## 🧩 Metodología
El proyecto se estructuró bajo la metodología **CRISP-DM**, con las siguientes etapas:

1. **Comprensión del problema**  
   Definición de las actividades a reconocer y de las características corporales relevantes (cadera, rodillas, tobillos, muñecas, hombros y cabeza).

2. **Recolección y anotación de datos**  
   - Uso de **MediaPipe** para extraer coordenadas clave de articulaciones humanas.  
   - Anotación manual y validación de datos para garantizar consistencia.

3. **Preparación de datos**  
   - Limpieza y normalización de coordenadas.  
   - División de los datos en conjuntos de entrenamiento y prueba.

4. **Modelado**  
   - Entrenamiento de un modelo supervisado de **clasificación multiclase**.  
   - Evaluación del desempeño mediante métricas de precisión, recall y F1-score.

5. **Evaluación y documentación**  
   - Comparación de resultados por tipo de actividad.  
   - Análisis del impacto del etiquetado en la efectividad del modelo.

---

## 🛠️ Tecnologías utilizadas
- **Python**
- **MediaPipe**
- **Scikit-learn**
- **Pandas / NumPy**
- **Matplotlib / Seaborn**
- **CRISP-DM framework**

---

## 📊 Resultados
El modelo logró identificar con precisión las actividades más estructuradas (caminar, girar) y mostró sensibilidad moderada en acciones con mayor variabilidad (sentarse, levantarse).  
Estos resultados evidencian la importancia de un **buen etiquetado y consistencia en las coordenadas** para mejorar la generalización del modelo.

---

## 👩‍💻 Autores 
**Karen Valeria Jurado**  
**Juan Camilo Tobar**  
**Isabella Hernández**  
Estudiante de Ingeniería de Sistemas e Ingeniería en Energía Inteligente  
📧 isabellahernandez@ieee.org  
🌍 [GitHub](https://github.com/isahrnd)  

---

## 🧾 Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo o adaptarlo para fines educativos y de investigación, mencionando la autoría original.

