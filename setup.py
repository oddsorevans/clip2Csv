"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['pystebinIngram.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'images_1024x1024.icns',
    'packages': ['clipboard', 'csv', 'os', 'datetime']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
