import unittest
from modelos.huron import Huron


class test_Boa(unittest.TestCase):
    
    def test_hacer_sonido(self):
        huron = Huron('Huron 1', 15, 2, 'Ecuador', 200)
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron('Huron 1', 15, 2, 'Ecuador', 2)
        self.assertEqual(huron.calcular_flete(), 30)

   