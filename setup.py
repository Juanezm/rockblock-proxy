from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='rockblock_proxy',
    packages=['rockblock_proxy'],
    python_requires='>=3.7, <4',
    install_requires=required
)
