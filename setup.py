from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(__file__)
with open(os.path.join(module_dir, "astro", "VERSION")) as version_file:
    version = version_file.read().strip()

setup(
    name="astro",
    version=version,
    description="A module for astronomical symbols and zodiac signs",
    author="Janusz Janicki",
    author_email="janusz.janicki@arest.pl",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)