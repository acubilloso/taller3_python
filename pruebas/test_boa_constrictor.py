import unittest
from modelos.boa_constrictor import Boa_constricor


class test_Boa(unittest.TestCase):
    
    def test_hacer_sonido(self):
        boa  = Boa_constricor(edad=1, peso=23, pais_origen="Colombia", impuestos=23, nombre="Boa 1", ratones_comidos=2)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        boa  = Boa_constricor(edad=1, peso=23, pais_origen="Colombia", impuestos=2, nombre="Boa 1", ratones_comidos=2)
        self.assertEqual(boa.calcular_flete(), 46)  

    def test_alimentar_boa(self):
        boa  = Boa_constricor(edad=1, peso=23, pais_origen="Colombia", impuestos=2, nombre="Boa 1", ratones_comidos=9)
        boa.comer_ratones()
        self.assertEqual(boa.get_ratones_comidos(), 10)
