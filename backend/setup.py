"""
How to properily write one of these?

Responsibilities
1. Describe the app
2. Initialize the skeleton of the database
"""

from setuptools import find_packages, setup

setup(
    name='reita_backend',
    version='0.0.1',
    packages=find_packages(),
    long_description='This is the GraphQL Sever behind the Reita reading app.',
    install_requires=[
        'Flask==1.0.2',
        'Flask-GraphQL==2.0.0',
        'graphene==2.1.3',
        'graphene-sqlalchemy==2.1.1',
        'SQLAlchemy==1.3.1'
    ],
    zip_safe=False,

)