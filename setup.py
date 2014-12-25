from setuptools import setup, find_packages

setup(
    name='potranslate',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/bahattincinic/potranslate',
    license='MIT',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    description='PO File translation with GoogleTranslate',
    entry_points={
        'console_scripts': [
            'potranslate = potranslate.__main__:main',
        ],
    },
    install_requires=[
        'polib',
        'clint',
        'goslate'
    ],
)
