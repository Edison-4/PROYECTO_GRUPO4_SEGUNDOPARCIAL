# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

from servicio_bancario import ServicioBancario


class Prestamo(ServicioBancario):
    """Representa una línea de crédito o préstamo financiero amortizable. Hereda de ServicioBancario."""

    def __init__(self, codigo: str, titular: str, anio_apertura: int, monto: float, anios_plazo: int):
        """Inicializa las propiedades del préstamo incluyendo el monto capitalizado y el tiempo de amortización."""
        super().__init__(codigo, titular, anio_apertura)
        self.__monto = monto
        self.__anios_plazo = anios_plazo

    @property
    def monto(self) -> float:
        """Obtiene el monto total adjudicado del préstamo."""
        return self.__monto

    @monto.setter
    def monto(self, valor: float):
        """Establece el capital del crédito asegurando que el valor supere a cero."""
        if valor <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__monto = valor

    @property
    def anios_plazo(self) -> int:
        """Obtiene la vigencia o plazo en años estipulado para la deuda."""
        return self.__anios_plazo

    @anios_plazo.setter
    def anios_plazo(self, valor: int):
        """Establece la duración del plazo en años garantizando que sea mayor a cero."""
        if valor <= 0:
            raise ValueError("El plazo debe ser mayor a cero")
        self.__anios_plazo = valor

    def calcular_costos(self) -> float:
        """Determina el recargo mensual aplicando una tasa fija por seguro de desgravamen."""
        seguro_desgravamen = self.__monto * 0.01
        return seguro_desgravamen

    def __str__(self) -> str:
        """Retorna el formato legible con los datos del crédito y su respectivo deudor."""
        return f"Prestamo: {self.titular} - Monto: {self.__monto} - Plazo: {self.__anios_plazo} anios"


if __name__ == "__main__":
    prestamo_prueba = Prestamo("P001", "Luiz Perez", 2026, 5000.0, 5)
    print(prestamo_prueba)
    print(prestamo_prueba.calcular_costos())
