from setuptools import setup, find_packages

setup(
    name='analyseModule',
    version='1.0',
    packages=find_packages(include=['analysepackage']),
    install_requires=['pandas', 'numpy'],
    url='https://github.com/londzy/Analyse_Functions',
    license='MIT',
    author='Kwande Skaap; Tony Masombuka; Londiwe Cele; Tsholofelo Mautjana; Mmapule Rachel Ramonyai ',
    author_email='tonyhughmahlasedi@gmail.com; tshmau002@gmail.com; mmapulerachel@gmail.com; celelondiwe3@gmail.com; kwande.skaap@gmail.com',
    description='This module consists of seven functions used to extract data from a set of tweets in a Pandas dataframe. Full description in readme.md',
    long_description=open('README.md').read()
)
