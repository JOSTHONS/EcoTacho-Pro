"""
Proyecto: EcoTacho Pro
Autor: Gaby (Josthyn)
Descripción: Servidor Flask para aplicación educativa ambiental.
"""

from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURACIÓN GLOBAL ---
# Se utiliza un diccionario centralizado para facilitar el mantenimiento.
# Si el periodo cambia, solo se edita aquí y se refleja en todo el sitio.
PROJECT_CONFIG = {
    "app_name": "EcoTacho Pro",
    "materia": "Tacho - Aplicación Ambiental",
    "cuatrimestre": "Quinto Cuatrimestre",
    "periodo_actual": "Enero - Junio" # Periodo académico solicitado
}

@app.route('/')
def index():
    """Renderiza la página de inicio con el Hero Section."""
    return render_template('index.html', 
                           title="Inicio", 
                           breadcrumb=["Inicio"], 
                           config=PROJECT_CONFIG)

@app.route('/sistema-ambiental')
def sistema():
    """Renderiza la información sobre el Sistema de Gestión Ambiental (SGA)."""
    return render_template('sistema.html', 
                           title="SGA", 
                           breadcrumb=["Inicio", "Sistema de Gestión"], 
                           config=PROJECT_CONFIG)

@app.route('/futuro')
def futuro():
    """Muestra la sección de concientización sobre las futuras generaciones."""
    return render_template('futuro.html', 
                           title="Futuro", 
                           breadcrumb=["Inicio", "Futuro del Planeta"], 
                           config=PROJECT_CONFIG)

@app.route('/tres-r')
def tres_r():
    """Sección interactiva sobre Reducir, Reutilizar y Reciclar."""
    return render_template('tres_r.html', 
                           title="Las 3 R", 
                           breadcrumb=["Inicio", "Las 3 R"], 
                           config=PROJECT_CONFIG)

if __name__ == '__main__':
    # Ejecución en modo debug para desarrollo (auto-recarga al guardar cambios)
    app.run(debug=True)