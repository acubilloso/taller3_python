from modelos.animal import Animal
from abc import ABC, abstractmethod
class Animal_exotico(Animal, ABC):

    def __init__(self, nombre:str, peso: float, edad : int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos =impuestos
        self.set_kilos_comidos(0)

    @property
    def pais_origen(self): 
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value):
        self._pais_origen = value

    @property
    def impuestos(self):
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value):
        self._impuestos = value

    def calcular_flete(self) -> float:
        return self.get_peso() * self.impuestos

    @abstractmethod
    def hacer_sonido(self):
        pass

    def comer(self, kilos):
        return self.set_kilos_comidos(self.get_kilos_comidos() + kilos)

    def obtener_kilos_comidos(self, kilos):
        return self.get_kilos_comidos()