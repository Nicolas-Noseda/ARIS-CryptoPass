import os

from setuptools import setup

setup(
    name='ARIS-CryptoPass',
    version='1.0.0',
    packages=['src', 'src.model', 'src.classes', 'src.widgets', 'src.widgets.password', 'src.windows'],
    url='',
    license='',
    author='Noseda Nicolas',
    author_email='nicolas.noseda.pro@gmail.com',
    description='Software to encrypt and save password and credit cards',
    data_files=[('/usr/share/applications', ['data/ARIS-CryptoPass.desktop']),
                ('/usr/local/share', ['data/IconPNG.png'])]
)
