from setuptools import setup, find_packages

setup(
    name='spider',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nltk==3.9.1',
    ],
)