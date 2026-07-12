# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# - Gordillo Diana
# - Vidal Jostin
# - Plaza Edison
# - Chalen Camila

import sys

from PySide6.QtWidgets import QApplication

from servicio.persona import PersonaServicio

app = QApplication()
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())