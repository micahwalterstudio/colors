from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='colors',
    version='0.1',
    description='',
    author='Micah Walter Studio',
    url='https://github.com/micahwalterstudio/colors',
    dependency_links=[
        'https://github.com/givp/RoyGBiv/tarball/master#egg=roygbiv',
        'https://github.com/micahwalterstudio/swatchbook/tarball/master#egg=swatchbook',
     ],
    install_requires=[
        'roygbiv',
        'swatchbook',
    ],
    requires=['roygbiv', 'swatchbook'],
    packages=packages,
    scripts=[],
    download_url='https://github.com/micahwalterstudio/colors/tarball/master',
    license='MIT')