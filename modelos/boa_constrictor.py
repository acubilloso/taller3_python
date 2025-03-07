from modelos.animal_exotico import Animal_exotico

class Boa_constricor(Animal_exotico):

    def __init__(self, nombre, peso, edad, pais_origen, impuestos, ratones_comidos: int):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = ratones_comidos

    def get_ratones_comidos(self):
        return self._ratones_comidos

    def set_ratones_comidos(self, value):
        self._ratones_comidos = value

    def hacer_sonido(self):
        return "¡Tsss!"
    
    def comer_ratones(self):
        ratones  = self.get_ratones_comidos() + 1
        if(ratones == 10):
            self.set_ratones_comidos(ratones)
        else:
            raise ValueError("Demasiados ratones")

