from abc import ABC, abstractmethod
from modelos.iAnimal import iAnimal
class Animal(iAnimal, ABC):

    def __init__(self, nombre : str, peso : float, edad : int):
       self.nombre = nombre
       self.peso = peso
       self.edad  = edad
       self.kilos_comidos = 0

    def get_kilos_comidos(self):
        return self.kilos_comidos

    def set_kilos_comidos(self, value):
        self.kilos_comidos = value

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_peso(self):
        return self.peso

    def set_peso(self, value):
        self.peso = value

    def get_edad(self):
        return self.edad

    def set_edad(self, value):
        self.edad = value

    @abstractmethod
    def comer(self, kilos):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self, kilos):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass