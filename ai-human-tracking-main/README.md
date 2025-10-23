# Sistema de Anotación de Video para Análisis de Movimientos

## Descripción del Proyecto
Este proyecto es el entregable final del curso **Inteligencia Artificial 1** de la Universidad ICESI, Facultad de Ingeniería, Diseño y Ciencias Aplicadas, semestre 2025-1. Desarrollado por un grupo de [2-3] estudiantes, el objetivo es crear una herramienta de software que analice actividades específicas de una persona (caminar hacia la cámara, caminar de regreso, girar, sentarse, ponerse de pie) en videos en tiempo real, utilizando técnicas de inteligencia artificial y analítica. La herramienta clasifica actividades y realiza un seguimiento de movimientos articulares y posturales, como inclinaciones laterales y ángulos de articulaciones clave.

El proyecto sigue la metodología **CRISP-DM** y utiliza herramientas como **MediaPipe** para el seguimiento de articulaciones y modelos supervisados (SVM, Random Forest, XGBoost) para la clasificación de actividades.

## Objetivos
- **Objetivo principal**: Desarrollar un sistema que clasifique actividades humanas en tiempo real a partir de videos y realice un seguimiento de articulaciones clave (cadera, rodillas, tobillos, muñecas, hombros, cabeza).
- **Objetivos específicos**:
  - Capturar y anotar un conjunto de datos de videos con personas realizando las actividades mencionadas.
  - Implementar un sistema de seguimiento de articulaciones usando MediaPipe.
  - Entrenar modelos de clasificación supervisada para identificar actividades.
  - Visualizar en tiempo real las actividades detectadas y métricas posturales (inclinaciones, ángulos) mediante una interfaz gráfica.

## Estructura del Repositorio
El repositorio está organizado en tres carpetas correspondientes a las entregas del proyecto:
- **Entrega1**: Pregunta de interés, metodología, métricas, análisis exploratorio de datos, estrategias para recolección de datos adicionales y análisis ético.
- **Entrega2**: Estrategia de obtención de datos, preprocesamiento, entrenamiento de modelos, resultados iniciales y plan de despliegue.
- **Entrega3**: Reducción de características, evaluación final, despliegue, reporte final y video de presentación.