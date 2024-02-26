from setuptools import setup, find_packages

setup(
    name='new_test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    url='https://github.com/dragsvillestar/new_function',
    author='Simon Negbejie',
    author_email='neggiehalo@gmail'
)