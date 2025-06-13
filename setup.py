from setuptools import setup

setup(
    name="window-bot",
    version="1.0",
    install_requires=[
        "python-telegram-bot>=20.3",
        "matplotlib>=3.7.1",
        "numpy>=1.24.3",
        "python-dotenv>=1.0.0"
    ],
    python_requires='>=3.10, <3.11',
)
