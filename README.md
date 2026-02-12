# 🌿 EcoTacho Pro: Ingeniería Web para la Sustentabilidad

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-v3.0.0-000000?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-v5.3.2-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Producción-success?style=for-the-badge)

## 📖 Resumen Ejecutivo

**EcoTacho Pro** es una plataforma web educativa de alto impacto diseñada para la concientización ambiental. Desarrollada por **Gaby (Josthyn)** para la materia **Tacho** en el **Quinto Cuatrimestre**, la aplicación integra principios de desarrollo moderno para gestionar información académica y ambiental de forma eficiente. El proyecto destaca por su enfoque en la **Experiencia de Usuario (UX)** y el **Diseño Responsivo**.

---

## 🛠️ Especificaciones Técnicas (Stack Tecnológico)

El desarrollo se fundamenta en un stack robusto enfocado en la escalabilidad:

- **Backend (Python/Flask):** Procesamiento de rutas dinámicas y lógica de servidor.
- **Frontend (HTML5/Jinja2):** Uso de herencia de plantillas para optimizar el código y evitar la redundancia.
- **Diseño (CSS3/Bootstrap 5):** Implementación de un sistema de rejilla (Grid) para adaptabilidad total a dispositivos móviles y escritorio.
- **Arquitectura:** Separación estricta entre lógica de negocio (`app.py`), recursos estáticos (`static/`) y vistas (`templates/`).

---

## 📸 Galería de Pruebas de Funcionamiento (Evidencia Visual)

A continuación, se documenta la interfaz de usuario final mediante las 4 pruebas de validación técnica realizadas:

|   🏠 1. Nodo de Inicio (User Experience)    | 📊 2. Sistema de Gestión Ambiental (SGA)  |
| :-----------------------------------------: | :---------------------------------------: |
|   ![Prueba 1](static/images/Prueba1.png)    |  ![Prueba 2](static/images/Prueba2.png)   |
| _Presentación impactante con Hero Section._ | _Documentación técnica sobre normativas._ |

| 🌎 3. Módulo de Concientización: Futuro |       ♻️ 4. Guía Práctica: Las 3 R        |
| :-------------------------------------: | :---------------------------------------: |
| ![Prueba 3](static/images/Prueba3.png)  |  ![Prueba 4](static/images/Prueba4.png)   |
| _Enfoque en preservación generacional._ | _Segmentación interactiva del reciclaje._ |

---

## 🏗️ Registro de Implementación Paso a Paso

### Fase 1: Entorno y Dependencias

Se inicializó un entorno virtual (`venv`) para aislar las dependencias del proyecto. Se instaló Flask y se configuró el archivo `requirements.txt` para asegurar la portabilidad del sistema.

### Fase 2: Desarrollo del Core (app.py)

Se programaron las rutas dinámicas asegurando que el **Periodo Académico: Enero - Junio** se inyectara de forma global en todas las vistas mediante un diccionario de configuración centralizado.

### Fase 3: Frontend y UX Pro

Se diseñó un archivo de estilos `style.css` personalizado con variables de color para fortalecer la identidad visual. Se implementaron **Breadcrumbs** dinámicos para mejorar la navegabilidad del usuario.

---

## 📂 Estructura del Repositorio

```text
EcoTacho-Pro/
├── app.py              # Cerebro de la aplicación (Python)
├── requirements.txt    # Dependencias del sistema
├── .gitignore          # Filtro de archivos para Git
├── README.md           # Documentación maestra
├── static/
│   ├── css/            # Estilos personalizados (style.css)
│   └── images/         # Recursos visuales y pruebas (.png, .jpg)
└── templates/          # Vistas HTML (Herencia de Jinja2)
```
