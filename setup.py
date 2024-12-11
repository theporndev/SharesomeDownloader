from setuptools import setup

setup(
    name="ssdownload",
    version="1.2",
    py_modules=["main"],  # Ensure the file is named `main.py`
    entry_points={
        "console_scripts": [
            "ssdownload=main:main",  # Matches the `main()` function in main.py
        ],
    },
)
