
# Define constants for zodiac names with prefix ZOD_
ZOD_ARIES       = "Aries"
ZOD_TAURUS      = "Taurus"
ZOD_GEMINI      = "Gemini"
ZOD_CANCER      = "Cancer"
ZOD_LEO         = "Leo"
ZOD_VIRGO       = "Virgo"
ZOD_LIBRA       = "Libra"
ZOD_SCORPIO     = "Scorpio"
ZOD_SAGITTARIUS = "Sagittarius"
ZOD_CAPRICORN   = "Capricorn"
ZOD_AQUARIUS    = "Aquarius"
ZOD_PISCES      = "Pisces"

# Define constants for zodiac symbols with prefix SYM_
SYM_ARIES       = "♈"
SYM_TAURUS      = "♉"
SYM_GEMINI      = "♊"
SYM_CANCER      = "♋"
SYM_LEO         = "♌"
SYM_VIRGO       = "♍"
SYM_LIBRA       = "♎"
SYM_SCORPIO     = "♏"
SYM_SAGITTARIUS = "♐"
SYM_CAPRICORN   = "♑"
SYM_AQUARIUS    = "♒"
SYM_PISCES      = "♓"

# Define date ranges for each zodiac sign as (month, day) tuples
DATES_ARIES     = ((3 , 21), (4 , 19))  # March 21 - April 19
DATES_TAURUS    = ((4 , 20), (5 , 20))  # April 20 - May 20
DATES_GEMINI    = ((5 , 21), (6 , 20))  # May 21 - June 20
DATES_CANCER    = ((6 , 21), (7 , 22))  # June 21 - July 22
DATES_LEO       = ((7 , 23), (8 , 22))  # July 23 - August 22
DATES_VIRGO     = ((8 , 23), (9 , 22))  # August 23 - September 22
DATES_LIBRA     = ((9 , 23), (10, 22))  # September 23 - October 22
DATES_SCORPIO   = ((10, 23), (11, 21))  # October 23 - November 21
DATES_SAGITTARIUS = ((11, 22), (12, 21))  # November 22 - December 21
DATES_CAPRICORN = ((12, 22), (1 , 19))  # December 22 - January 19
DATES_AQUARIUS  = (( 1, 20), (2 , 18))  # January 20 - February 18
DATES_PISCES    = (( 2, 19), (3 , 20))  # February 19 - March 20

class Zodiacs:
    zodiacs = {
        SYM_ARIES: (ZOD_ARIES, DATES_ARIES),
        SYM_TAURUS: (ZOD_TAURUS, DATES_TAURUS),
        SYM_GEMINI: (ZOD_GEMINI, DATES_GEMINI),
        SYM_CANCER: (ZOD_CANCER, DATES_CANCER),
        SYM_LEO: (ZOD_LEO, DATES_LEO),
        SYM_VIRGO: (ZOD_VIRGO, DATES_VIRGO),
        SYM_LIBRA: (ZOD_LIBRA, DATES_LIBRA),
        SYM_SCORPIO: (ZOD_SCORPIO, DATES_SCORPIO),
        SYM_SAGITTARIUS: (ZOD_SAGITTARIUS, DATES_SAGITTARIUS),
        SYM_CAPRICORN: (ZOD_CAPRICORN, DATES_CAPRICORN),
        SYM_AQUARIUS: (ZOD_AQUARIUS, DATES_AQUARIUS),
        SYM_PISCES: (ZOD_PISCES, DATES_PISCES)
    }

    @classmethod
    def name(self, symbol):
        """Retrieve the name of the zodiac sign given its symbol."""
        return self.zodiacs.get(symbol, (None, None))[0]  # Return name or None if not found

    @classmethod
    def symbol(self, name):
        """Retrieve the symbol of the zodiac sign given its name."""
        for sym, (zodiac_name, _) in self.zodiacs.items():
            if zodiac_name == name:
                return sym
        return None  # Return None if the name is not found

    @classmethod
    def zodiac_names(self):
        """Return a list of all zodiac sign names."""
        return [name for _, (name, _) in self.zodiacs.items()]

    @classmethod
    def zodiac_symbols(self):
        """Return a list of all zodiac symbols."""
        return list(self.zodiacs.keys())

    @classmethod
    def date_range(self, symbol):
        """Retrieve the date range of the zodiac sign given its symbol."""
        return self.zodiacs.get(symbol, (None, (None, None)))[1]  # Return date range or None if not found

    @classmethod
    def date_range_by_name(self, name):
        """Retrieve the date range of the zodiac sign given its name."""
        for sym, (zodiac_name, dates) in self.zodiacs.items():
            if zodiac_name == name:
                return dates
        return None  # Return None if the name is not found

if __name__ == "__main__":
    zodiacs = Zodiacs()
    print(zodiacs.name(SYM_ARIES))                  # Output: Aries
    print(zodiacs.symbol(ZOD_ARIES))                # Output: ♈
    print(zodiacs.date_range(SYM_ARIES))            # Output: ((3, 21), (4, 19))
    print(zodiacs.date_range_by_name(ZOD_ARIES))    # Output: ((3, 21), (4, 19))