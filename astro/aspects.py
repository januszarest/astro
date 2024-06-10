
# Define constants for aspect symbols with prefix SYM_
SYM_CONJUNCTION = "☌"               # 0
SYM_OPPOSITION  = "☍"               # 180
SYM_TRINE       = "△"              # 120
SYM_SQUARE      = "□"               # 90
SYM_SEXTILE     = "⚹"               # 60
SYM_QUINCUNX    = "⚷"               # 72

# Define constants for aspect names with prefix AS_
AS_CONJUNCTION  = "Conjunction"     # 0
AS_OPPOSITION   = "Opposition"      # 180
AS_TRINE        = "Trine"           # 120    
AS_SQUARE       = "Square"          # 90
AS_SEXTILE      = "Sextile"         # 60
AS_QUINCUNX     = "Quincunx"        # 72

class Aspects:

    # Dictionary to store aspect symbols and their names using constants
    aspects = {
        SYM_CONJUNCTION: AS_CONJUNCTION,
        SYM_OPPOSITION: AS_OPPOSITION,
        SYM_TRINE: AS_TRINE,
        SYM_SQUARE: AS_SQUARE,
        SYM_SEXTILE: AS_SEXTILE,
        SYM_QUINCUNX: AS_QUINCUNX
    }

    @classmethod
    def name(cls, symbol):
        """Retrieve the name of the aspect given its symbol."""
        return cls.aspects.get(symbol, None)  # Return None if the symbol is not found

    @classmethod
    def symbol(cls, name):
        """Retrieve the symbol of the aspect given its name."""
        for sym, aspect_name in cls.aspects.items():
            if aspect_name == name:
                return sym
        return None  # Return None if the name is not found

    @classmethod
    def aspect_names(cls):
        """Return a list of all aspect names."""
        return list(cls.aspects.values())

    @classmethod
    def aspect_symbols(cls):
        """Return a list of all aspect symbols."""
        return list(cls.aspects.keys())

if __name__ == "__main__":

    aspects = Aspects()

    print(aspects.name(SYM_CONJUNCTION))     # Output: Conjunction
    print(aspects.symbol(AS_CONJUNCTION))    # Output: ☌

