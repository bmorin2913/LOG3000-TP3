import unittest
from backend.operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """
    Classe de tests unitaires pour les fonctions du module operators.py.
    Chaque méthode teste une opération mathématique et vérifie que les erreurs sont détectées.
    """

    def test_add(self):
        """
        Teste la fonction add pour différents cas.
        Vérifie que l'addition fonctionne correctement.
        """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)

    def test_negative_operation(self):
        """
        Teste les opérations avec un nombre négatif.
        Vérifie que les fonctions gèrent correctement les valeurs négatives.
        """
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(divide(6, -2), -3)

    def test_subtract(self):
        """
        Teste la fonction subtract pour différents cas.
        Vérifie que la soustraction fonctionne correctement.
        """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """
        Teste la fonction multiply pour différents cas.
        Vérifie que la multiplication fonctionne correctement.
        """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        """
        Teste la fonction divide pour différents cas.
        Vérifie que la division entière fonctionne correctement et que la division par zéro soulève une exception.
        """
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
