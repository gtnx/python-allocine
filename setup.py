from distutils.core import setup

setup(
    name='allocine-wrapper',
    version='0.1.0',
    author='Guillaume Thomas',
    author_email='guillaume.thomas642@gmail.com',
    packages=['allocine'],
    scripts=[],
    url='http://pypi.python.org/pypi/python-allocine/',
    license='LICENSE.txt',
    description='Wrapper of Allocine API',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)