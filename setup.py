from setuptools import setup, find_packages

setup(
    name="quantum-numerical-methods-project",
    version="0.1.0",
    description="Applied mathematics project for analytical and numerical solutions of the 1D infinite potential well.",
    author="Pablo Torres, Omar Mohamed, Pablo Garma, Adam Bajer and Noa Keseric",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
    extras_require={
        "dev": ["pytest"],
    },
    python_requires=">=3.10",
)