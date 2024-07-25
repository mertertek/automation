from setuptools import setup

APP = ['main.py']
DATA_FILES = ['automation.html']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'bs4', 're'],
    'plist': {
        'CFBundleName': 'siu',
        'CFBundleIdentifier': 'com.example.siu',
        'CFBundleVersion': '1.0',
        'CFBundleExecutable': 'siu',
        'LSMinimumSystemVersion': '10.15',
    }
}

setup(
    name='siu',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'beautifulsoup4==4.12.3',
        'bs4==0.0.2',
        'altgraph==0.17.4',
        'macholib==1.16.3',
        'modulegraph==0.19.6',
        'packaging==24.1',
        'py2app==0.28.8',
        'setuptools==71.1.0',
        'soupsieve==2.5',
    ],
)
