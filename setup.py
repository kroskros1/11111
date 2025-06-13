from setuptools import setup

setup(
    name="window-bot",
    version="1.0",
    install_requires=[
        "python-telegram-bot==20.3",
        "matplotlib==3.8.0",
        "numpy==1.24.4",  # Змінено версію
        "python-dotenv==1.0.0"
    ],
    python_requires='>=3.9, <3.11',  # Додано обмеження
)
