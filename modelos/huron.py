
from modelos.animal_exotico import Animal_exotico
class Huron(Animal_exotico):

    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
    
    def hacer_sonido(self):
        return "¡Eek Eek!"
    