from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package to calculate Gann swings'
LONG_DESCRIPTION = 'Package to take a set of OHLC data and calculate Gann swings from it'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="gannswings", 
        version=VERSION,
        author="David Mitchell",
        author_email="<monch1962+gannswings@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'financial-analysis', 'technical-analysis', 'trading', 'gann'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)