from PySide6.QtWidgets import QMainWindow, QMessageBox
from GUI.vtn_principal import Ui_vtn_principal
from datos.banco_DAO import BancoDAO
from dominio.servicio_bancario import ServicioBancario


class PersonaServicio(QMainWindow):

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)

        # Conexión de eventos de la interfaz
        self.ui.btn_agregar.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_buscar.clicked.connect(self.buscar)
        self.ui.btn_actualizar.clicked.connect(self.actualizar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)

    def guardar(self):
        titular = self.ui.txt_titular.text().strip()
        codigo = self.ui.txt_codigo.text().strip()
        anioapertura = self.ui.txt_anioapertura.text().strip()
        email = self.ui.txt_email.text().strip()

        # 1. Validar campos obligatorios vacíos
        if titular == '' or codigo == '' or anioapertura == '' or email == '':
            QMessageBox.information(self, "Advertencia", "Por favor, complete todos los campos obligatorios")
            return

        # 2. Validación tradicional para el formato del correo electrónico
        if '@' not in email or '.' not in email:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un correo electrónico válido")
            return

        try:
            servicio = ServicioBancario(codigo=codigo, titular=titular, anio_apertura=int(anioapertura))
            if BancoDAO.insertar(servicio, email) == 1:
                self.ui.statusbar.showMessage('Registro guardado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'Error al guardar el registro en la base de datos')
        except ValueError:
            QMessageBox.warning(self, "Error de tipo", "El año de apertura debe ser un número entero válido")
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error inesperado: {e}')

    def buscar(self):
        codigo_buscar = self.ui.txt_buscar_codigo.text().strip()
        if codigo_buscar == '':
            QMessageBox.information(self, "Advertencia", "Ingrese un código en el campo de búsqueda")
            return

        servicio = BancoDAO.seleccionar_x_codigo(codigo_buscar)
        if servicio:
            self.ui.txt_codigo.setText(servicio.codigo)
            self.ui.txt_titular.setText(servicio.titular)
            self.ui.txt_anioapertura.setText(str(servicio.anio_apertura))
            self.ui.txt_email.setText(getattr(servicio, 'email', ''))
            self.ui.statusbar.showMessage('Registro cargado exitosamente', 3000)
        else:
            QMessageBox.information(self, "Información", "No se encontró ningún registro con ese código")

    def actualizar(self):
        titular = self.ui.txt_titular.text().strip()
        codigo = self.ui.txt_codigo.text().strip()
        anioapertura = self.ui.txt_anioapertura.text().strip()
        email = self.ui.txt_email.text().strip()

        if titular == '' or codigo == '' or anioapertura == '' or email == '':
            QMessageBox.information(self, "Advertencia", "Complete todos los campos del formulario para actualizar")
            return

        if '@' not in email or '.' not in email:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un correo electrónico válido")
            return

        try:
            servicio = ServicioBancario(codigo=codigo, titular=titular, anio_apertura=int(anioapertura))
            if BancoDAO.actualizar(servicio, email) == 1:
                self.ui.statusbar.showMessage('Registro actualizado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'No se pudo actualizar el registro. Verifique el código.')
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error: {e}')

    def eliminar(self):
        codigo_buscar = self.ui.txt_buscar_codigo.text().strip()
        if codigo_buscar == '':
            QMessageBox.information(self, "Advertencia",
                                    "Ingrese el código del registro que desea eliminar en el campo de búsqueda")
            return

        try:
            if BancoDAO.eliminar(codigo_buscar) == 1:
                self.ui.statusbar.showMessage('Registro eliminado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'No se encontró el registro para eliminar')
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error: {e}')

    def limpiar(self):
        self.ui.txt_titular.clear()
        self.ui.txt_codigo.clear()
        self.ui.txt_anioapertura.clear()
        self.ui.txt_email.clear()
        self.ui.txt_buscar_codigo.clear()