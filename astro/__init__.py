import os

module_dir = os.path.dirname(__file__)
with open(os.path.join(module_dir, "VERSION")) as version_file:
    __version__ = version_file.read().strip()

from .planets import Planets
from .aspects import Aspects
from .zodiacs import Zodiacs

__all__ = ["Planets", "Aspects", "Zodiacs"]