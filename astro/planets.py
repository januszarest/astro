
# Define constants for planet names with prefix PL_
PL_SUN          = "Sun"
PL_MOON         = "Moon"
PL_MERCURY      = "Mercury"
PL_VENUS        = "Venus"
PL_MARS         = "Mars"
PL_JUPITER      = "Jupiter"
PL_SATURN       = "Saturn"
PL_URANUS       = "Uranus"
PL_NEPTUNE      = "Neptune"
PL_PLUTO        = "Pluto"

PL_NORTH_NODE   = "North Node"
PL_SOUTH_NODE   = "South Node"
PL_ASCENDANT    = "Ascendant"
PL_MIDHEAVEN    = "Midheaven"

# Define constants for planet symbols with prefix SYM_
SYM_SUN         = "☉"
SYM_MOON        = "☽"
SYM_MERCURY     = "☿"
SYM_VENUS       = "♀"
SYM_MARS        = "♂"
SYM_JUPITER     = "♃"
SYM_SATURN      = "♄"
SYM_URANUS      = "♅"
SYM_NEPTUNE     = "♆"
SYM_PLUTO       = "♇"

SYM_NORTH_NODE  = "☊"
SYM_SOUTH_NODE  = "☋"
SYM_ASCENDANT   = "Ⓐ"
SYM_MIDHEAVEN   = "Ⓘ"

class Planets:

    # Dictionary to store planet names and their symbols
    planets_symbols = {
        PL_SUN: SYM_SUN,
        PL_MOON: SYM_MOON,
        PL_MERCURY: SYM_MERCURY,
        PL_VENUS: SYM_VENUS,
        PL_MARS: SYM_MARS,
        PL_JUPITER: SYM_JUPITER,
        PL_SATURN: SYM_SATURN,
        PL_URANUS: SYM_URANUS,
        PL_NEPTUNE: SYM_NEPTUNE,
        PL_PLUTO: SYM_PLUTO,
        PL_NORTH_NODE: SYM_NORTH_NODE,
        PL_SOUTH_NODE: SYM_SOUTH_NODE,
        PL_ASCENDANT: SYM_ASCENDANT,
        PL_MIDHEAVEN: SYM_MIDHEAVEN    
    }

    @classmethod
    def name(self, symbol):
        """Retrieve the name of the planet given its symbol."""
        for name, sym in self.planets_symbols.items():
            if sym == symbol:
                return name
        return None  # Return None if the symbol is not found

    @classmethod
    def symbol(self, name):
        """Retrieve the symbol of the planet given its name."""
        return self.planets_symbols.get(name, None)  # Return None if the name is not found

    @classmethod
    def planets(self):
        """Return a list of all planet names."""
        return list(self.planets_symbols.keys())

    @classmethod
    def symbols(self):
        """Return a list of all planet symbols."""
        return list(self.planets_symbols.values())


if __name__ == "__main__":

    planets = Planets()

    print(planets.name("☉"))         # Output: Sun
    print(planets.symbol("Sun"))      # Output: ☉