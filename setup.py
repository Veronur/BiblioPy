from setuptools import setup

setup(name='dev_luccadc',
    version='0.1',
    author='Lucca Delchiaro Costabile',
    packages=['dev_aberto'],
    install_requires=['requests'],
    scripts=['scripts/hello.py'],
    classifiers=['Operating System :: Microsoft :: Windows','Programming Language :: Python :: 3.7']
    )