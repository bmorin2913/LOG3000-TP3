import unittest
from app import calculate
from flask import Flask
import os

class TestAppCalculate(unittest.TestCase):
    """
    Tests unitaires pour la fonction calculate du fichier app.py.
    Permet de détecter les erreurs de logique et de gestion des cas limites.
    """

    def test_valid_add(self):
        """
        Teste l'addition avec des valeurs valides.
        Vérifie que calculate retourne le bon résultat pour l'opérateur '+'.
        """
        self.assertEqual(calculate("2+3"), 5)
        self.assertEqual(calculate("-1+1"), 0)
        self.assertEqual(calculate("0+0"), 0)

    def test_valid_subtract(self):
        """
        Teste la soustraction avec des valeurs valides.
        Vérifie que calculate retourne le bon résultat pour l'opérateur '-'.
        """
        self.assertEqual(calculate("5-3"), 2)
        self.assertEqual(calculate("-1-1"), -2)

    def test_valid_multiply(self):
        """
        Teste la multiplication avec des valeurs valides.
        Vérifie que calculate retourne le bon résultat pour l'opérateur '*'.
        """
        self.assertEqual(calculate("2*3"), 6)
        self.assertEqual(calculate("-2*3"), -6)
        self.assertEqual(calculate("0*10"), 0)

    def test_valid_divide(self):
        """
        Teste la division entière avec des valeurs valides.
        Vérifie que calculate retourne le bon résultat pour l'opérateur '/'.
        """
        self.assertEqual(calculate("6/3"), 2)
        self.assertEqual(calculate("5/2"), 2.5)

    def test_invalid_empty(self):
        """
        Teste les cas où l'expression est vide ou None.
        Vérifie que calculate soulève une ValueError.
        """
        with self.assertRaises(ValueError):
            calculate("")
        with self.assertRaises(ValueError):
            calculate(None)

    def test_invalid_format(self):
        """
        Teste les expressions mal formées (opérateur au début/fin, plusieurs opérateurs).
        Vérifie que calculate soulève une ValueError.
        """
        with self.assertRaises(ValueError):
            calculate("+23")
        with self.assertRaises(ValueError):
            calculate("23+")
        with self.assertRaises(ValueError):
            calculate("2++3")
        with self.assertRaises(ValueError):
            calculate("2+3-4")

    def test_invalid_operands(self):
        """
        Teste les cas où les opérandes ne sont pas des nombres.
        Vérifie que calculate soulève une ValueError.
        """
        with self.assertRaises(ValueError):
            calculate("a+3")
        with self.assertRaises(ValueError):
            calculate("2+b")
        with self.assertRaises(ValueError):
            calculate("a+b")

    def test_divide_by_zero(self):
        """
        Teste la division par zéro.
        Vérifie que calculate soulève une ZeroDivisionError.
        """
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")

    def test_display_format(self):
        """
        Teste que le résultat retourné est bien affiché.
        """
        self.assertEqual(str(calculate("2+3")), "5")
        self.assertEqual(str(calculate("5/2")), "2.5")
        self.assertEqual(str(calculate("5-3")), "2")
        self.assertEqual(str(calculate("2*3")), "6")
        self.assertEqual(str(calculate("0+0")), "0")

    def test_button_labels(self):
        """
        Teste que les labels des boutons sont corrects dans le template HTML.
        Vérifie qu'il n'y a pas de labels incorrects et que tous les chiffres et opérateurs sont présents.
        """
        template_path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        with open(template_path, 'r', encoding='utf-8') as f:
            html = f.read()
        missing = []
        # Vérifie tous les chiffres
        for n in range(0, 10):
            if f'>{n}<' not in html:
                missing.append(f"chiffre '{n}'")
        # Vérifie les opérateurs
        for op in ['+', '-', '*', '/']:
            if f'>{op}<' not in html:
                missing.append(f"opérateur '{op}'")
        if missing:
            self.fail("Boutons manquants ou incorrects : " + ", ".join(missing))

if __name__ == '__main__':
    unittest.main()
