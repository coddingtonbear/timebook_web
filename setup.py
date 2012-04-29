from setuptools import setup

from timebook import get_version

setup(
    name='timebook_web',
    version=get_version(),
    url='http://bitbucket.org/latestrevision/timebook_web/',
    description='Be transparent.',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['timebook_web',],
    install_requires = [
            'Flask',
            'timebook'
        ]
)
