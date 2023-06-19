"""Esse arquivo testa o arquivo main.py"""

import unittest  # para criar o caso de teste

from main import is_prime, list_prime_factors


class TestFunction(unittest.TestCase):
    """Classe para testar o arquivo main.py"""

    def setUp(self):
        """Cria um dicionário com os números e seus fatores primos."""
        self.nums = {
            1: [],
            2: [2],
            3: [3],
            4: [2, 2],
            21: [3, 7],
            56: [2, 2, 2, 7],
            83: [83],
            97: [97],
            120: [2, 2, 2, 3, 5],
        }

    def test_list_prime_factors(self):
        """Testa a função list_prime_factors"""
        for key, value in self.nums.items():
            self.assertEqual(list_prime_factors(key), value)

    def test_is_prime(self):
        """Testa a função is_prime"""
        for key, value in self.nums.items():
            if len(value) == 1:
                self.assertTrue(is_prime(key))
            else:
                self.assertFalse(is_prime(key))
