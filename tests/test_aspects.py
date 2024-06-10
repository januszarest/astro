import unittest
from astro.aspects import Aspects

class TestAspects(unittest.TestCase):

    def setUp(self):
        self.aspects = Aspects()

    def test_name(self):
        self.assertEqual(self.aspects.name("☌"), "Conjunction")
        self.assertEqual(self.aspects.name("☍"), "Opposition")
        self.assertEqual(self.aspects.name("△"), "Trine")
        self.assertEqual(self.aspects.name("□"), "Square")
        self.assertEqual(self.aspects.name("⚹"), "Sextile")
        self.assertEqual(self.aspects.name("⚷"), "Quincunx")
        self.assertIsNone(self.aspects.name("invalid_symbol"))

    def test_symbol(self):
        self.assertEqual(self.aspects.symbol("Conjunction"), "☌")
        self.assertEqual(self.aspects.symbol("Opposition"), "☍")
        self.assertEqual(self.aspects.symbol("Trine"), "△")
        self.assertEqual(self.aspects.symbol("Square"), "□")
        self.assertEqual(self.aspects.symbol("Sextile"), "⚹")
        self.assertEqual(self.aspects.symbol("Quincunx"), "⚷")
        self.assertIsNone(self.aspects.symbol("Invalid Name"))

    def test_aspect_names(self):
        expected_names = ["Conjunction", "Opposition", "Trine", "Square", "Sextile", "Quincunx"]
        self.assertCountEqual(self.aspects.aspect_names(), expected_names)

    def test_aspect_symbols(self):
        expected_symbols = ["☌", "☍", "△", "□", "⚹", "⚷"]
        self.assertCountEqual(self.aspects.aspect_symbols(), expected_symbols)

if __name__ == "__main__":
    unittest.main()
