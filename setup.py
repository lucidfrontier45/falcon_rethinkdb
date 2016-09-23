try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    "falcon",
    "rethinkdb",
    "jsonschema",
    "toolz"
]

setup(
    name='falcon_rethinkdb',
    version='0.1',
    packages=['falcon_rethinkdb'],
    url='https://github.com/lucidfrontier45/falcon_rethinkdb',
    license='Apache License version 2',
    author='Shiqiao Du',
    author_email='lucidfrontier.45@gmail.com',
    description='',
    install_requires=install_requires
)
