import unittest
from astro.planets import Planets

class TestPlanets(unittest.TestCase):

    def setUp(self):
        self.planets = Planets()

    def test_name(self):
        self.assertEqual(self.planets.name("☉"), "Sun")
        self.assertEqual(self.planets.name("☽"), "Moon")
        self.assertEqual(self.planets.name("☿"), "Mercury")
        self.assertEqual(self.planets.name("♀"), "Venus")
        self.assertEqual(self.planets.name("♂"), "Mars")
        self.assertEqual(self.planets.name("♃"), "Jupiter")
        self.assertEqual(self.planets.name("♄"), "Saturn")
        self.assertEqual(self.planets.name("♅"), "Uranus")
        self.assertEqual(self.planets.name("♆"), "Neptune")
        self.assertEqual(self.planets.name("♇"), "Pluto")
        self.assertEqual(self.planets.name("☊"), "North Node")
        self.assertEqual(self.planets.name("☋"), "South Node")
        self.assertEqual(self.planets.name("Ⓐ"), "Ascendant")
        self.assertEqual(self.planets.name("Ⓘ"), "Midheaven")
        self.assertIsNone(self.planets.name("invalid_symbol"))

    def test_symbol(self):
        self.assertEqual(self.planets.symbol("Sun"), "☉")
        self.assertEqual(self.planets.symbol("Moon"), "☽")
        self.assertEqual(self.planets.symbol("Mercury"), "☿")
        self.assertEqual(self.planets.symbol("Venus"), "♀")
        self.assertEqual(self.planets.symbol("Mars"), "♂")
        self.assertEqual(self.planets.symbol("Jupiter"), "♃")
        self.assertEqual(self.planets.symbol("Saturn"), "♄")
        self.assertEqual(self.planets.symbol("Uranus"), "♅")
        self.assertEqual(self.planets.symbol("Neptune"), "♆")
        self.assertEqual(self.planets.symbol("Pluto"), "♇")
        self.assertEqual(self.planets.symbol("North Node"), "☊")
        self.assertEqual(self.planets.symbol("South Node"), "☋")
        self.assertEqual(self.planets.symbol("Ascendant"), "Ⓐ")
        self.assertEqual(self.planets.symbol("Midheaven"), "Ⓘ")
        self.assertIsNone(self.planets.symbol("Invalid Name"))

    def test_planets(self):
        expected_planets = [
            "Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn",
            "Uranus", "Neptune", "Pluto", "North Node", "South Node",
            "Ascendant", "Midheaven"
        ]
        self.assertCountEqual(self.planets.planets(), expected_planets)

    def test_symbols(self):
        expected_symbols = [
            "☉", "☽", "☿", "♀", "♂", "♃", "♄", "♅", "♆", "♇", "☊", "☋",
            "Ⓐ", "Ⓘ"
        ]
        self.assertCountEqual(self.planets.symbols(), expected_symbols)

if __name__ == "__main__":
    unittest.main()
