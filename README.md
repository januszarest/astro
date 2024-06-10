# Astro

**Astro** is a Python module designed to work with astronomical symbols and zodiac signs. It provides classes to easily retrieve information about planets, astrological aspects, and zodiac signs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

## Features

- **Planet Symbols**: Retrieve names and symbols of planets.
- **Astrological Aspects**: Retrieve names and symbols of astrological aspects.
- **Zodiac Signs**: Retrieve names, symbols, and date ranges of zodiac signs.

## Installation

To install the module, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/januszarest/astro.git
    cd astro
    ```

2. **Install the Module**:

    You can install the module locally using `pip`:

    ```bash
    pip install .
    ```

3. **Install in Editable Mode**:

    If you are working on developing the module, install it in editable mode:

    ```bash
    pip install -e .
    ```

## Usage

Below are examples of how to use the module. For more information, check the documentation in the source code.

### Planets

```python
from astro.planets_symbols import PlanetSymbols

planets = PlanetSymbols()
print(planets.name("☉"))  # Output: Sun
print(planets.symbol("Sun"))  # Output: ☉
```

### Astrological Aspects

```
from astro.aspects_symbols import AspectSymbols

aspects = AspectSymbols()
print(aspects.name("☌"))  # Output: Conjunction
print(aspects.symbol("Conjunction"))  # Output: ☌
```

### Zodiac Signs

```
from astro.zodiac_symbols import ZodiacSymbols

zodiacs = ZodiacSymbols()
print(zodiacs.name("♈"))  # Output: Aries
print(zodiacs.date_range("♈"))  # Output: ((3, 21), (4, 19))
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

MIT License
The MIT License is a permissive free software license that allows software to be freely used, modified, and distributed. This means you can:

Use the software for any purpose, including commercial applications.
Modify the software to suit your needs.
Distribute the software, including modified versions.
The only condition is that the original license and copyright notice must be included in any distributed copies or substantial portions of the software.

## Author
Janusz Janicki - januszarest@gmail.com

Feel free to reach out if you have any questions or need further assistance with the module.
Thank you for using Astro! We hope it helps with your astronomical and astrological projects.
