from setuptools import setup,find_packages

VERSION = "0.0.1"
DESCRIPTION = "AstroThur"
LONG_DESCRIPTION = "Arthur's Astrophysics Python Package"

# Setting up
setup(
    name="astrothur",
    version=VERSION,
    author="Arthur E. B. Pasqualotto",
    author_email="arthur.pasqualotto@acad.ufsm.br",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['astronomy','astrophysics','stellar'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)