# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila


class Sucursal:
    """Representa una agencia o sucursal física de la entidad bancaria."""

    def __init__(self, nombre: str, ciudad: str, anio_inauguracion: int):
        """Inicializa la sucursal con su nombre identificativo, ubicación y año de apertura."""
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__anio_inauguracion = anio_inauguracion

    @property
    def nombre(self) -> str:
        """Obtiene el nombre único asignado a la sucursal."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre de la sucursal validando que contenga caracteres válidos."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre de la sucursal no puede estar vacío")
        self.__nombre = valor

    @property
    def ciudad(self) -> str:
        """Obtiene la ciudad donde opera físicamente la sucursal."""
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, valor: str):
        """Establece la ciudad de ubicación de la sucursal tras verificar la validez."""
        if not valor or valor.strip() == "":
            raise ValueError("La ciudad no puede estar vacía")
        self.__ciudad = valor

    @property
    def anio_inauguracion(self) -> int:
        """Obtiene el año en que la sucursal fue inaugurada oficialmente."""
        return self.__anio_inauguracion

    @anio_inauguracion.setter
    def anio_inauguracion(self, valor: int):
        """Establece el año de inauguración verificando que el entero sea estrictamente positivo."""
        if valor <= 0:
            raise ValueError("El año de inauguración debe ser mayor a cero")
        self.__anio_inauguracion = valor

    def __str__(self) -> str:
        """Retorna la información clave sobre la localización de la sucursal."""
        return f"Sucursal {self.__nombre} ubicada en {self.__ciudad}"


if __name__ == "__main__":
    sucursal_prueba = Sucursal("Centro", "Guayaquil", 2010)
    print(sucursal_prueba)
