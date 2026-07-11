# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila


class Cliente:
    """Representa a un cliente registrado en la entidad financiera."""

    def __init__(self, identificacion: str, nombre: str, anio_nacimiento: int):
        """Inicializa un objeto Cliente con sus datos personales esenciales."""
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__anio_nacimiento = anio_nacimiento

    @property
    def identificacion(self) -> str:
        """Obtiene el documento de identidad o cédula del cliente."""
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor: str):
        """Establece el documento de identidad tras validar que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("La identificación no puede estar vacía")
        self.__identificacion = valor

    @property
    def nombre(self) -> str:
        """Obtiene el nombre completo del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre completo tras validar que no sea una cadena vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = valor

    @property
    def anio_nacimiento(self) -> int:
        """Obtiene el año de nacimiento del cliente."""
        return self.__anio_nacimiento

    @anio_nacimiento.setter
    def anio_nacimiento(self, valor: int):
        """Establece el año de nacimiento asegurando que sea mayor que cero."""
        if valor <= 0:
            raise ValueError("El año de nacimiento debe ser mayor a cero")
        self.__anio_nacimiento = valor

    def __str__(self) -> str:
        """Retorna la representación textual de los datos del cliente."""
        return f"Cliente: {self.__nombre} - ID: {self.__identificacion}"


if __name__ == "__main__":
    cliente_prueba = Cliente("0987654321", "Luis Perez", 2004)
    print(cliente_prueba)
