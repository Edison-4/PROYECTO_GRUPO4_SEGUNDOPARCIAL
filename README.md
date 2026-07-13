# [cite_start]Proyecto Segundo Parcial GUI con Base de Datos [cite: 111]
# [cite_start]Asignatura: Programación Orientada a Objetos [cite: 112]
# [cite_start]Jornada: [Escribe aquí: Matutina o Vespertina] [cite: 113, 126]
# [cite_start]Grupo: [Escribe aquí el número o nombre del grupo] [cite: 114]
# [cite_start]Integrantes: [cite: 115, 125]
# Gordillo Diana
# Vidal Jostin
# Edison P.
# Chalen Camila

---

## [cite_start]1. Título del proyecto [cite: 123]
Sistema de Administración de Servicios Bancarios

## [cite_start]2. Descripción general del sistema [cite: 124]
Es una aplicación de escritorio diseñada para gestionar servicios bancarios y cuentas de clientes. [cite_start]El sistema permite registrar, consultar, actualizar y eliminar (CRUD) información de manera intuitiva a través de una interfaz gráfica conectada en tiempo real a una base de datos relacional[cite: 36].

## [cite_start]3. Funcionalidades implementadas [cite: 127]
* Registro de nuevas cuentas bancarias con validación de datos.
* Búsqueda y visualización de registros mediante código único.
* Actualización de datos de clientes existentes.
* Eliminación segura de registros de la base de datos.
* Limpieza automática del formulario.

## [cite_start]4. Tecnologías utilizadas [cite: 128]
* **Lenguaje de Programación:** Python 3
* **Biblioteca Gráfica:** PySide6 (Qt)
* **Base de Datos:** SQL Server
* **Conector de Base de Datos:** pyodbc
* **Control de Versiones:** Git y GitHub

## [cite_start]5. Instrucciones para ejecutar el proyecto [cite: 129]
1. Clonar este repositorio en tu máquina local.
2. Instalar las dependencias necesarias ejecutando: `pip install PySide6 pyodbc`
3. Configurar la base de datos ejecutando el script SQL proporcionado en tu servidor de SQL Server.
4. Ajustar las credenciales de conexión (`_SERVIDOR`, `_USUARIO`, `_PASSWORD`) en el archivo `datos/conexion.py`.
5. Ejecutar el archivo raíz: `python main.py`

## [cite_start]6. Estructura del proyecto [cite: 130]
[cite_start]A continuación, se detalla la arquitectura modular del proyecto separando la interfaz, la lógica de negocio y el acceso a datos[cite: 102]:

```mermaid
graph TD
    A[main.py] --> B(servicio/persona.py : Controlador)
    B --> C{GUI/vtn_principal.py : Interfaz}
    B --> D[dominio/servicio_bancario.py : Lógica]
    B --> E[datos/banco_DAO.py : Acceso a Datos]
    E --> F[(datos/conexion.py : SQL Server)]
