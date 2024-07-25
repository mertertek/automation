from setuptools import setup

APP = ['main.py']
DATA_FILES = ['automation.html']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'bs4', 're'],
}

setup(
    name='Siu Html Updater',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
