from setuptools import setup, find_packages

setup(
    name="crime_test",       # Package name
    version="1.0.0",         # Package version
    description="A package for validating and cleaning crime data",
    long_description=open("README.md").read(),  
    author="Ji Soo Kim",                  # Your name
    author_email="jisoo.kim01@sjsu.edu",  # Your email
    url="https://github.com/CS131-BigDataProcessing/mini-assignments-Kimjisoo1710",
    packages=find_packages(),             # Automatically find the package
    install_requires=[                    # List of dependencies
        "pandas",
        "numpy",
    ],
)
