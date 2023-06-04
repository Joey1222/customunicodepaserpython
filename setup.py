from setuptools import setup, find_packages

setup(
    name='Custom Unicode Paser',
    version='1.0.0',
    description='A Custom unicode paser',
    author='Joseph Kuntson',
    author_email='jmknutson2012@gmail.com',
    url='https://github.com/Joey1222/customunicodepaserpython',
    packages=find_packages(include=['Paser', 'Paser.*']),
    setup_requires=['setuptools'],
    classifiers=["License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python :: 3 :: Only"]
)
