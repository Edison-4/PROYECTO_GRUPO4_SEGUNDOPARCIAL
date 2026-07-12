# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# -
# -
# -
# -

class ServicioBancario:
    """Clase base que representa un servicio bancario general dentro del sistema."""

    def __init__(self, codigo: str, titular: str, anio_apertura: int):
        """Inicializa los atributos esenciales del servicio bancario."""
        self.__codigo = codigo
        self.__titular = titular
        self.__anio_apertura = anio_apertura

    @property
    def codigo(self) -> str:
        """Obtiene el código identificador del servicio bancario."""
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str):
        """Establece el código del servicio bancario tras validar que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El código no puede estar vacío")
        self.__codigo = valor

    @property
    def titular(self) -> str:
        """Obtiene el nombre del titular asignado al servicio."""
        return self.__titular

    @titular.setter
    def titular(self, valor: str):
        """Establece el titular del servicio bancario tras validar que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El titular no puede estar vacío")
        self.__titular = valor

    @property
    def anio_apertura(self) -> int:
        """Obtiene el año en que se realizó la apertura del servicio."""
        return self.__anio_apertura

    @anio_apertura.setter
    def anio_apertura(self, valor: int):
        """Establece el año de apertura verificando que sea un valor mayor a cero."""
        if valor <= 0:
            raise ValueError("El año de apertura debe ser mayor a cero")
        self.__anio_apertura = valor

    def calcular_costos(self):
        """Calcula los costos mensuales asociados al servicio bancario.

        Este método está diseñado para ser sobrescrito por las clases hijas.
        """
        pass

    def __str__(self) -> str:
        """Retorna una representación formateada del servicio bancario en cadena."""
        return f"{self.__codigo} - {self.__titular} - {self.__anio_apertura}"


if __name__ == "__main__":
    servicio_prueba = ServicioBancario("S001", "Luis Perez", 2024)
    print(servicio_prueba)