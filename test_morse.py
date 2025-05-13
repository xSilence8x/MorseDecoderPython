"""
Testovací modul pro Morseův enkodér a dekodér.
Obsahuje unit testy pro funkce 'encode_to_morse' a 'decode_from_morse'.

"""

import unittest
from unittest.mock import patch
from morse import encode_to_morse, decode_from_morse, run_morse_program


class TestMorseFunctions(unittest.TestCase):

    def test_encode_to_morse(self):
        """
        Unit testy pro funkce encode_to_morse a decode_from_morse.
        Testuje běžné, hraniční i chybové případy.
        """
        self.assertEqual(encode_to_morse("sos"), "... --- ...")
        self.assertEqual(encode_to_morse("sos test"),
                         "... --- ... / - . ... -")
        self.assertEqual(encode_to_morse("sos!"), "... --- ... -.-.--")
        self.assertEqual(encode_to_morse("sos! sos"),
                         "... --- ... -.-.-- // ... --- ...")
        self.assertEqual(encode_to_morse("abc#"), ".- -... -.-. ?")
        self.assertEqual(encode_to_morse(""), "Prázdný vstup.")

    def test_decode_from_morse(self):
        """
        Testuje převod Morseova kódu zpět do textu.
        Ověřuje dekódování slov, vět, neplatných znaků a oddělovačů.
        """
        self.assertEqual(decode_from_morse("... --- ..."), "SOS")
        self.assertEqual(decode_from_morse("... --- ... / ... --- ..."),
                         "SOS SOS")
        self.assertEqual(decode_from_morse(
            "... --- ... -.-.-- // ... --- ..."), "SOS! SOS"
            )
        self.assertEqual(decode_from_morse("....--"), "?")
        self.assertEqual(decode_from_morse("/ / //"), "   ")
        self.assertEqual(decode_from_morse(""), "Prázdný vstup.")

    def test_run_morse_program(self):
        """
        Testuje, zda program správně zpracuje zakódování 'sos' a ukončení.
        """
        with patch('builtins.input', side_effect=['e', 'sos', 'k']):
            run_morse_program()
        with patch('builtins.input', side_effect=['d', '... --- ...', 'k']):
            run_morse_program()
        with patch('builtins.input', side_effect=['x', 'k']):
            run_morse_program()


if __name__ == "__main__":
    unittest.main()
