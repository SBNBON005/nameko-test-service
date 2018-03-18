import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = [f.read()]


setup(
    name='test_service',
    version='0.0.1',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Framework :: Nameko',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Bongani Sibanda',
    author_email='sibandabongz@gmail.com',
    packages=find_packages(),
    zip_safe=True,
    install_requires=requires,
)
