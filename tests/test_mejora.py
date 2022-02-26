import unittest
from KataTDD.mejora import Mejora

class TestMejora(unittest.TestCase):

    def test_conjunto_vacio(self):
        mejora = Mejora([])
        self.assertIsNone(mejora.promedio())

    def test_conjunto_un_elemento(self):
        mejora = Mejora([5])
        self.assertEqual (mejora.promedio(), 5)

    def test_conjunto_dos_elementos(self):
        mejora = Mejora([5,7])
        self.assertEqual (mejora.promedio(), 6)

    def test_conjunto_n_elementos(self):
        mejora = Mejora([2,4,8,9,10,15])
        self.assertEqual(mejora.promedio(), (2+4+8+9+10+15)/6)