from setuptools import setup, find_packages

requires = [
    'nameko==2.8.4',
    'requests==2.18.4'
]


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
