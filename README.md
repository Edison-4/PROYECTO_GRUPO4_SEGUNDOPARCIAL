# Proyecto Segundo Parcial GUI con Base de Datos
**Asignatura:** Programación Orientada a Objetos

---

## 1. Título del proyecto
**Sistema de Administración de Servicios Bancarios**

## 2. Descripción general del sistema
Es una aplicación de escritorio diseñada para gestionar servicios bancarios y cuentas de clientes. El sistema permite registrar, consultar, actualizar y eliminar (CRUD) información de manera intuitiva a través de una interfaz gráfica conectada en tiempo real a una base de datos relacional.

## 3. Integrantes del grupo
* Gordillo Diana
* Vidal Jostin
* Edison P.
* Chalen Camila

## 4. Jornada
* **Jornada:** Vespertina
* **Grupo:** 4
## 5. Funcionalidades implementadas
El sistema cumple con el ciclo completo de operaciones CRUD:
* **Registro (Create):** Permite ingresar nuevas cuentas bancarias en la base de datos con validación previa.
* **Consulta (Read):** Búsqueda y visualización de los datos de un cliente mediante su código único.
* **Actualización (Update):** Modificación de los datos de un registro existente.
* **Eliminación (Delete):** Borrado seguro de registros dentro de la base de datos.
* **Limpieza:** Reseteo automático de todos los campos del formulario de la interfaz.

## 6. Tecnologías utilizadas
* **Lenguaje de Programación:** Python 3
* **Biblioteca Gráfica:** PySide6 (Qt)
* **Base de Datos:** SQL Server
* **Conector de Base de Datos:** pyodbc
* **Control de Versiones:** Git y GitHub

## 7. Instrucciones para ejecutar el proyecto
1. Clonar este repositorio en la máquina local.
2. Instalar las dependencias necesarias ejecutando en la terminal: `pip install PySide6 pyodbc`
3. Ejecutar el script SQL proporcionado (en el código o anexo) para crear la base de datos `SAP` y la tabla `objeto` en SQL Server.
4. Ajustar las credenciales de conexión (`_SERVIDOR`, `_USUARIO`, `_PASSWORD`) dentro del archivo `datos/conexion.py` según la configuración de tu servidor local.
5. Ejecutar el archivo raíz para iniciar la aplicación: `python main.py`

## 8. Descripción de la base de datos
Se utiliza una base de datos relacional denominada `SAP` que contiene una tabla principal llamada `objeto` con la siguiente estructura de columnas:
* **IDCuenta:** `INT IDENTITY(1,1) PRIMARY KEY` (Autoincrementable).
* **codigo:** `VARCHAR(10) UNIQUE NOT NULL` (Identificador alfanumérico).
* **titular:** `VARCHAR(100) NOT NULL` (Nombre del cliente).
* **anio_apertura:** `INT NOT NULL` (Año de creación de la cuenta).
* **email:** `VARCHAR(100) NOT NULL` (Correo de contacto).
* **tipo_cuenta:** `VARCHAR(50) NOT NULL` (Ej. Cuenta Ahorro, Cuenta Corriente).

## 9. Capturas de pantalla de la GUI
![Ventana Principal de la GUI](REEMPLAZA_ESTO_CON_EL_LINK_DE_TU_IMAGEN_DE_LA_INTERFAZ)
> *Figura 1: Interfaz gráfica principal mostrando los campos de entrada, el ComboBox y los botones de acción.*

## 10. Evidencia de conexión a la base de datos
![Registros en SQL Server](REEMPLAZA_ESTO_CON_EL_LINK_DE_TU_IMAGEN_DE_SQL_SERVER)
> *Figura 2: Consulta SELECT en SQL Server demostrando que los datos ingresados desde la GUI se almacenan correctamente en la tabla.*

## 11. Enlace al video demostrativo
[▶️ Haz clic aquí para ver el video demostrativo del sistema (Demostración CRUD)](REEMPLAZA_ESTO_CON_EL_LINK_DE_TU_VIDEO)

## 12. Explicación breve de las validaciones implementadas
Para asegurar la integridad de la base de datos, el sistema valida la información antes de procesar cualquier transacción:
* **Campos obligatorios:** Se verifica mediante condicionales que ningún campo de texto esté vacío.
* **Formato de correo electrónico:** Se comprueba lógicamente la existencia de los caracteres obligatorios `@` y `.` en el campo de email.
* **Tipos de datos numéricos:** Se aplica un bloque `try-except` capturando `ValueError` para garantizar que el "Año de apertura" sea estrictamente un número entero (evitando que el programa se cierre por errores de tipo).
* **Selección válida (ComboBox):** Se restringe la acción de guardar o actualizar si el usuario deja el tipo de cuenta en la opción por defecto ("Seleccionar").

## 13. Estado final del proyecto
Proyecto finalizado, documentado y 100% funcional cumpliendo con todos los requisitos de la rúbrica.

## 14. Estructura del proyecto
El proyecto aplica una arquitectura modular que separa la interfaz gráfica, la lógica de negocio y el acceso a datos.

```mermaid
graph TD
    A[main.py] --> B(servicio/persona.py : Controlador)
    B --> C{GUI/vtn_principal.py : Interfaz Visual}
    B --> D[dominio/servicio_bancario.py : Dominio/Lógica]
    B --> E[datos/banco_DAO.py : Acceso a Datos]
    E --> F[(SQL Server : Base de Datos)]
