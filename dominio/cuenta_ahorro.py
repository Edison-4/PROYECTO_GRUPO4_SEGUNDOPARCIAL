# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

from servicio_bancario import ServicioBancario


class CuentaAhorro(ServicioBancario):
    """Representa una cuenta de ahorros tradicional. Hereda de ServicioBancario."""

    def __init__(self, codigo: str, titular: str, anio_apertura: int, saldo: float, tasa_interes: float):
        """Inicializa los datos compartidos de la clase base junto con saldo e interés específicos."""
        super().__init__(codigo, titular, anio_apertura)
        self.__saldo = saldo
        self.__tasa_interes = tasa_interes

    @property
    def saldo(self) -> float:
        """Obtiene el saldo monetario actual de la cuenta."""
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        """Establece el saldo de la cuenta validando que no sea un saldo negativo."""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = valor

    @property
    def tasa_interes(self) -> float:
        """Obtiene la tasa de interés anualizada de la cuenta de ahorros."""
        return self.__tasa_interes

    @tasa_interes.setter
    def tasa_interes(self, valor: float):
        """Establece la tasa de interés validando que no se asigne un porcentaje negativo."""
        if valor < 0:
            raise ValueError("La tasa de interés no puede ser negativa")
        self.__tasa_interes = valor

    def calcular_costos(self) -> float:
        """Retorna el costo plano por mantenimiento mensual para las cuentas de ahorros."""
        mantenimiento = 5.0
        return mantenimiento

    def __str__(self) -> str:
        """Retorna una descripción concisa que detalla el titular y el saldo actual."""
        return f"Cuenta Ahorro: {self.titular} - Saldo: {self.__saldo}"


if __name__ == "__main__":
    cuenta_prueba = CuentaAhorro("C001", "Carlos Martinez", 2026, 1500.0, 0.03)
    print(cuenta_prueba)
    print(cuenta_prueba.calcular_costos())
