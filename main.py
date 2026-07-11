import sys

from PySide6.QtWidgets import QApplication

from servicio.persona import PersonaServicio

app = QApplication()
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())