from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='wh2o',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.1.0',
    description='Python bindings for American Whitewater's GraphQL endpoint.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)