import unittest
from astro.zodiacs import Zodiacs

class TestZodiacSymbols(unittest.TestCase):

    def setUp(self):
        # Setting up an instance of the class for tests
        self.zodiac = Zodiacs()

    def test_name(self):
        self.assertEqual(self.zodiac.name("♈"), "Aries")
        self.assertEqual(self.zodiac.name("♉"), "Taurus")
        self.assertEqual(self.zodiac.name("♊"), "Gemini")
        self.assertIsNone(self.zodiac.name("invalid_symbol"))

    def test_symbol(self):
        self.assertEqual(self.zodiac.symbol("Aries"), "♈")
        self.assertEqual(self.zodiac.symbol("Taurus"), "♉")
        self.assertEqual(self.zodiac.symbol("Gemini"), "♊")
        self.assertIsNone(self.zodiac.symbol("Invalid Name"))

    def test_zodiac_names(self):
        expected_names = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
                          "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        self.assertCountEqual(self.zodiac.zodiac_names(), expected_names)

    def test_zodiac_symbols(self):
        expected_symbols = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏",
                            "♐", "♑", "♒", "♓"]
        self.assertCountEqual(self.zodiac.zodiac_symbols(), expected_symbols)

    def test_date_range(self):
        self.assertEqual(self.zodiac.date_range("♈"), ((3, 21), (4, 19)))
        self.assertEqual(self.zodiac.date_range("♉"), ((4, 20), (5, 20)))
        self.assertEqual(self.zodiac.date_range("♊"), ((5, 21), (6, 20)))
        self.assertEqual(self.zodiac.date_range("invalid_symbol"), (None, None))

    def test_date_range_by_name(self):
        self.assertEqual(self.zodiac.date_range_by_name("Aries"), ((3, 21), (4, 19)))
        self.assertEqual(self.zodiac.date_range_by_name("Taurus"), ((4, 20), (5, 20)))
        self.assertEqual(self.zodiac.date_range_by_name("Gemini"), ((5, 21), (6, 20)))
        self.assertIsNone(self.zodiac.date_range_by_name("Invalid Name"), (None, None))

if __name__ == "__main__":
    unittest.main()