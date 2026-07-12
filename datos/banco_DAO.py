# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# - Gordillo Diana
# - Vidal Jostin
# - Plaza Edison
# - Chalen Camila

from datos.conexion import Conexion
from dominio.servicio_bancario import ServicioBancario

class BancoDAO:
    """Data Access Object (DAO) para las operaciones CRUD en la base de datos."""
    _INSERT = "INSERT INTO objeto (codigo, titular, anio_apertura, email) VALUES (?, ?, ?, ?)"
    _SELECT = "SELECT codigo, titular, anio_apertura, email FROM objeto WHERE codigo = ?"
    _UPDATE = "UPDATE objeto SET titular = ?, anio_apertura = ?, email = ? WHERE codigo = ?"
    _DELETE = "DELETE FROM objeto WHERE codigo = ?"
    _SELECT_TODOS = "SELECT codigo, titular, anio_apertura, email FROM objeto"

    @classmethod
    def insertar(cls, servicio, email):
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (servicio.codigo, servicio.titular, servicio.anio_apertura, email)
                cursor.execute(cls._INSERT, datos)
                contador_registros = cursor.rowcount
        except Exception as e:
            print(f"Error en insertar: {e}")
            contador_registros = -1
        return contador_registros

    @classmethod
    def seleccionar_x_codigo(cls, codigo):
        servicio = None
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (codigo, )
                cursor.execute(cls._SELECT, datos)
                rs = cursor.fetchone()
                if rs:
                    servicio = ServicioBancario(codigo=rs[0], titular=rs[1], anio_apertura=int(rs[2]))
                    # Se asigna dinámicamente el email como atributo del objeto para la GUI
                    servicio.email = rs[3]
        except Exception as e:
            print(f"Error en seleccionar_x_codigo: {e}")
            servicio = None
        return servicio

    @classmethod
    def actualizar(cls, servicio, email):
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (servicio.titular, servicio.anio_apertura, email, servicio.codigo)
                cursor.execute(cls._UPDATE, datos)
                contador_registros = cursor.rowcount
        except Exception as e:
            print(f"Error en actualizar: {e}")
            contador_registros = -1
        return contador_registros

    @classmethod
    def eliminar(cls, codigo):
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (codigo, )
                cursor.execute(cls._DELETE, datos)
                contador_registros = cursor.rowcount
        except Exception as e:
            print(f"Error en eliminar: {e}")
            contador_registros = -1
        return contador_registros

    @classmethod
    def seleccionar_todos(cls):
        servicios = list()
        try:
            with Conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECT_TODOS)
                rs = cursor.fetchall()
                for registro in rs:
                    servicio = ServicioBancario(codigo=registro[0], titular=registro[1], anio_apertura=int(registro[2]))
                    servicio.email = registro[3]
                    servicios.append(servicio)
        except Exception as e:
            print(f"Error en seleccionar_todos: {e}")
            servicios = list()
        return servicios